"""
Progress tracking service for managing user task completion.
"""

from datetime import datetime
from typing import List, Optional, Dict
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.models.user import User
from app.models.task import Task
from app.models.progress import UserProgress


class ProgressService:
    """Service for tracking user progress on tasks."""

    @staticmethod
    def get_user_progress(db: Session, user_id: int) -> List[UserProgress]:
        """
        Get all progress records for a user.

        Args:
            db: Database session
            user_id: User ID

        Returns:
            List of user progress records
        """
        return db.query(UserProgress).filter(UserProgress.user_id == user_id).all()

    @staticmethod
    def get_task_progress(
        db: Session, user_id: int, task_id: int
    ) -> Optional[UserProgress]:
        """
        Get progress for a specific task.

        Args:
            db: Database session
            user_id: User ID
            task_id: Task ID

        Returns:
            UserProgress if exists, None otherwise
        """
        return (
            db.query(UserProgress)
            .filter(
                and_(UserProgress.user_id == user_id, UserProgress.task_id == task_id)
            )
            .first()
        )

    @staticmethod
    def mark_task(
        db: Session,
        user_id: int,
        task_id: int,
        status: str,
        notes: Optional[str] = None,
    ) -> UserProgress:
        """
        Mark a task with a status (not_started, in_progress, completed).

        Args:
            db: Database session
            user_id: User ID
            task_id: Task ID
            status: Status (not_started, in_progress, completed)
            notes: Optional notes

        Returns:
            Updated or created UserProgress

        Raises:
            ValueError: If status is invalid or task doesn't exist
        """
        # Validate status
        valid_statuses = ["not_started", "in_progress", "completed"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")

        # Check if task exists
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise ValueError(f"Task {task_id} not found")

        # Get or create progress record
        progress = ProgressService.get_task_progress(db, user_id, task_id)

        if not progress:
            progress = UserProgress(user_id=user_id, task_id=task_id, status=status)
            db.add(progress)
        else:
            progress.status = status
            progress.updated_at = datetime.utcnow()

        # Update timestamps based on status
        if status == "in_progress" and not progress.started_at:
            progress.started_at = datetime.utcnow()
        elif status == "completed":
            if not progress.started_at:
                progress.started_at = datetime.utcnow()
            progress.completed_at = datetime.utcnow()
        elif status == "not_started":
            progress.started_at = None
            progress.completed_at = None

        # Update notes if provided
        if notes is not None:
            progress.notes = notes

        db.commit()
        db.refresh(progress)

        return progress

    @staticmethod
    def get_sprint_progress(db: Session, user_id: int, sprint_id: int) -> Dict:
        """
        Get progress summary for a sprint.

        Args:
            db: Database session
            user_id: User ID
            sprint_id: Sprint ID

        Returns:
            Dictionary with progress statistics
        """
        # Get all tasks in sprint
        tasks = db.query(Task).filter(Task.sprint_id == sprint_id).all()
        total_tasks = len(tasks)

        if total_tasks == 0:
            return {
                "sprint_id": sprint_id,
                "total_tasks": 0,
                "completed": 0,
                "in_progress": 0,
                "not_started": 0,
                "completion_percentage": 0,
            }

        # Get progress for each task
        task_ids = [task.id for task in tasks]
        progress_records = (
            db.query(UserProgress)
            .filter(
                and_(
                    UserProgress.user_id == user_id, UserProgress.task_id.in_(task_ids)
                )
            )
            .all()
        )

        # Count by status
        status_counts = {"completed": 0, "in_progress": 0, "not_started": 0}

        progress_map = {p.task_id: p for p in progress_records}

        for task in tasks:
            if task.id in progress_map:
                status = progress_map[task.id].status
                status_counts[status] = status_counts.get(status, 0) + 1
            else:
                status_counts["not_started"] += 1

        completion_percentage = (status_counts["completed"] / total_tasks) * 100

        return {
            "sprint_id": sprint_id,
            "total_tasks": total_tasks,
            "completed": status_counts["completed"],
            "in_progress": status_counts["in_progress"],
            "not_started": status_counts["not_started"],
            "completion_percentage": round(completion_percentage, 2),
        }

    @staticmethod
    def get_team_progress(db: Session, team: str) -> List[Dict]:
        """
        Get progress for all users in a team.

        Args:
            db: Database session
            team: Team name

        Returns:
            List of user progress summaries
        """
        users = db.query(User).filter(User.team == team).all()

        team_progress = []
        for user in users:
            # Get all user progress
            progress_records = (
                db.query(UserProgress).filter(UserProgress.user_id == user.id).all()
            )

            # Count by status
            status_counts = {"completed": 0, "in_progress": 0, "not_started": 0}

            for progress in progress_records:
                status_counts[progress.status] = (
                    status_counts.get(progress.status, 0) + 1
                )

            total_tasks = db.query(Task).count()
            tracked_tasks = len(progress_records)
            untracked = total_tasks - tracked_tasks

            team_progress.append(
                {
                    "user_id": user.id,
                    "user_name": user.name,
                    "user_email": user.email,
                    "completed": status_counts["completed"],
                    "in_progress": status_counts["in_progress"],
                    "not_started": status_counts["not_started"] + untracked,
                    "total_tasks": total_tasks,
                    "completion_percentage": (
                        round((status_counts["completed"] / total_tasks) * 100, 2)
                        if total_tasks > 0
                        else 0
                    ),
                }
            )

        return team_progress
