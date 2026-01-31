
import pytest
from unittest.mock import MagicMock, Mock
from datetime import datetime
from sqlalchemy.orm import Session

from app.services.progress_service import ProgressService
from app.models.user import User
from app.models.task import Task
from app.models.progress import UserProgress

@pytest.fixture
def mock_db():
    return MagicMock(spec=Session)

class TestProgressService:

    def test_mark_task_valid_new(self, mock_db):
        """Test marking a task that has no previous progress."""
        user_id = 1
        task_id = 100
        status = "in_progress"
        
        # Mock task existence
        mock_task = Task(id=task_id)
        # Mock query sequence: 
        # 1. query(Task).filter(...).first() -> returns task
        # 2. query(UserProgress).filter(...).first() -> returns None (no progress yet)
        mock_db.query.return_value.filter.return_value.first.side_effect = [mock_task, None]
        
        result = ProgressService.mark_task(mock_db, user_id, task_id, status)
        
        assert result.user_id == user_id
        assert result.task_id == task_id
        assert result.status == status
        assert result.started_at is not None
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()

    def test_mark_task_with_notes(self, mock_db):
        """Test marking a task and adding notes."""
        user_id = 1
        task_id = 100
        notes = "My notes"
        
        mock_task = Task(id=task_id)
        # 1. Check Task Exists, 2. Get existing progress (None)
        mock_db.query.return_value.filter.return_value.first.side_effect = [mock_task, None]
        
        result = ProgressService.mark_task(mock_db, user_id, task_id, "in_progress", notes=notes)
        
        assert result.notes == notes
        mock_db.commit.assert_called_once()

    def test_mark_task_update_status(self, mock_db):
        """Test updating status of an existing task."""
        user_id = 1
        task_id = 100
        old_progress = UserProgress(
            user_id=user_id, 
            task_id=task_id, 
            status="not_started",
            started_at=None
        )
        
        mock_task = Task(id=task_id)
        # 1. Check Task Exists, 2. Get existing progress
        mock_db.query.return_value.filter.return_value.first.side_effect = [mock_task, old_progress]
        
        result = ProgressService.mark_task(mock_db, user_id, task_id, "completed")
        
        assert result.status == "completed"
        assert result.started_at is not None 
        assert result.completed_at is not None
        mock_db.commit.assert_called_once()

    def test_mark_task_invalid_status(self, mock_db):
        """Test error when status is invalid."""
        with pytest.raises(ValueError, match="Invalid status"):
            ProgressService.mark_task(mock_db, 1, 1, "super_done")

    def test_mark_task_not_found(self, mock_db):
        """Test error when task doesn't exist."""
        # Task existence check returns None
        mock_db.query.return_value.filter.return_value.first.return_value = None
        
        with pytest.raises(ValueError, match="Task 999 not found"):
            ProgressService.mark_task(mock_db, 1, 999, "completed")

    def test_mark_task_reset_to_not_started(self, mock_db):
        """Test resetting a task clears timestamps."""
        user_id = 1
        task_id = 100
        existing_progress = UserProgress(
            user_id=user_id, task_id=task_id, status="completed", 
            started_at=datetime.utcnow(), completed_at=datetime.utcnow()
        )
        mock_task = Task(id=task_id)
        mock_db.query.return_value.filter.return_value.first.side_effect = [mock_task, existing_progress]

        result = ProgressService.mark_task(mock_db, user_id, task_id, "not_started")
        
        assert result.status == "not_started"
        assert result.started_at is None
        assert result.completed_at is None

    def test_get_sprint_progress_empty(self, mock_db):
        """Test sprint progress calculation with no tasks."""
        # Return empty list of tasks
        mock_db.query.return_value.filter.return_value.all.return_value = []
        
        result = ProgressService.get_sprint_progress(mock_db, user_id=1, sprint_id=99)
        
        assert result["total_tasks"] == 0
        assert result["completion_percentage"] == 0

    def test_get_sprint_progress_calculation(self, mock_db):
        """Test sprint progress percentage calculation."""
        user_id = 1
        sprint_id = 5
        
        tasks = [Task(id=1, sprint_id=sprint_id), Task(id=2, sprint_id=sprint_id)]
        progress_records = [
            UserProgress(user_id=user_id, task_id=1, status="completed")
        ]
        
        # 1. Get tasks in sprint
        # 2. Get user progress for those tasks
        mock_db.query.return_value.filter.return_value.all.side_effect = [tasks, progress_records]
        
        result = ProgressService.get_sprint_progress(mock_db, user_id, sprint_id)
        
        assert result["total_tasks"] == 2
        assert result["completed"] == 1
        assert result["not_started"] == 1
        assert result["completion_percentage"] == 50.0

    def test_get_team_progress(self, mock_db):
        """Test team progress retrieval."""
        team_name = "Avengers"
        users = [
            User(id=1, name="Tony", email="tony@stark.com", team=team_name),
            User(id=2, name="Steve", email="steve@rogers.com", team=team_name)
        ]
        
        user1_progress = [UserProgress(status="completed"), UserProgress(status="completed")]
        user2_progress = [UserProgress(status="in_progress")]
        
        # Mock sequence:
        # 1. Get users in team
        # 2. Get progress for user 1
        # 3. Get total tasks count (for user 1 calc)
        # 4. Get progress for user 2
        # 5. Get total tasks count (for user 2 calc)
        
        # Force count to return 10
        mock_db.query.return_value.count.return_value = 10
        
        # Handling the loop and query structure for getting progress is tricky with basic mocks side_effect
        # Easier approach: Mock filter().all() sequence
        mock_db.query.return_value.filter.return_value.all.side_effect = [
            users,
            user1_progress,
            user2_progress
        ]

        result = ProgressService.get_team_progress(mock_db, team_name)
        
        assert len(result) == 2
        # Tony: 2 completed out of 10 = 20%
        assert result[0]["user_name"] == "Tony"
        assert result[0]["completed"] == 2
        assert result[0]["completion_percentage"] == 20.0
        
        # Steve: 1 in_progress out of 10 = 0% completed (but tracked)
        assert result[1]["user_name"] == "Steve"
        assert result[1]["completed"] == 0
        assert result[1]["in_progress"] == 1
        assert result[1]["completion_percentage"] == 0.0

