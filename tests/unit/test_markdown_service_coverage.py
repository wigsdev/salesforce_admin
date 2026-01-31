import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from app.services.markdown_service import MarkdownService


class TestMarkdownServiceCoverage:

    @pytest.fixture
    def markdown_service(self):
        return MarkdownService()

    def test_get_file_path_missing(self, markdown_service):
        """Test getting path for non-existent file returns None."""
        with patch.object(Path, "exists", return_value=False):
            result = markdown_service.get_file_path("ghost.md")
            assert result is None

    def test_read_markdown_file_not_found(self, markdown_service):
        """Test reading non-existent file returns None."""
        with patch.object(markdown_service, "get_file_path", return_value=None):
            result = markdown_service.read_markdown("missing.md")
            assert result is None

    def test_read_markdown_exception(self, markdown_service):
        """Test handling of read errors (e.g. permission denied)."""
        # Mock get_file_path to return a valid-looking path
        mock_path = Path("protected.md")
        with patch.object(markdown_service, "get_file_path", return_value=mock_path):
            # Mock open to raise exception
            with patch("builtins.open", side_effect=PermissionError("Boom")):
                result = markdown_service.read_markdown("protected.md")
                assert result is None

    def test_list_directory_not_exists(self, markdown_service):
        """Test listing non-existent directory returns empty list."""
        with patch.object(Path, "exists", return_value=False):
            result = markdown_service.list_directory("invalid_dir")
            assert result == []

    def test_list_directory_not_dir(self, markdown_service):
        """Test listing a file as if it were a directory returns empty list."""
        with patch.object(Path, "exists", return_value=True):
            with patch.object(Path, "is_dir", return_value=False):
                result = markdown_service.list_directory("file.md")
                assert result == []

    def test_get_content_tree_not_exists(self, markdown_service):
        """Test getting tree for invalid path returns empty list."""
        with patch.object(Path, "exists", return_value=False):
            result = markdown_service.get_content_tree("invalid_path")
            assert result == []

    def test_extract_title_fallback(self, markdown_service):
        """Test title extraction falls back to filename if no H1."""
        content = "## Subtitle\nText"
        title = markdown_service._extract_title(content, "folder/my_cool_doc.md")
        assert title == "My Cool Doc"

    def test_list_directory_success(self, markdown_service):
        """Test listing directory with files and subdirectories."""
        # Create mock items
        mock_file = MagicMock(spec=Path)
        mock_file.is_file.return_value = True
        mock_file.is_dir.return_value = False
        mock_file.name = "doc.md"
        mock_file.stem = "doc"
        mock_file.suffix = ".md"
        mock_file.relative_to.return_value = Path("folder/doc.md")
        # Allow sorting
        mock_file.__lt__ = lambda self, other: self.name < other.name

        mock_dir = MagicMock(spec=Path)
        mock_dir.is_file.return_value = False
        mock_dir.is_dir.return_value = True
        mock_dir.name = "subfolder"
        mock_dir.relative_to.return_value = Path("folder/subfolder")
        mock_dir.__lt__ = lambda self, other: self.name < other.name

        # Mock hidden file
        mock_hidden = MagicMock(spec=Path)
        mock_hidden.is_dir.return_value = True
        mock_hidden.name = ".git"
        mock_hidden.__lt__ = lambda self, other: self.name < other.name

        with patch.object(Path, "exists", return_value=True):
            with patch.object(Path, "is_dir", return_value=True):
                with patch.object(
                    Path, "iterdir", return_value=[mock_file, mock_dir, mock_hidden]
                ):
                    result = markdown_service.list_directory("folder")

                    assert len(result) == 2
                    names = [r["name"] for r in result]
                    assert "doc" in names
                    assert "subfolder" in names

    def test_get_content_tree_recursive(self, markdown_service):
        """Test recursive content tree generation."""

        # Mock creation helper
        def create_mock_path(name, is_dir=False):
            p = MagicMock(spec=Path)
            p.name = name
            p.is_dir.return_value = is_dir
            p.is_file.return_value = not is_dir
            p.suffix = ".md" if not is_dir else ""
            p.relative_to.return_value = Path(name)
            # Add __lt__ just in case, though key sorting handles most
            p.__lt__ = lambda self, other: self.name < other.name
            return p

        file1 = create_mock_path("file1.md")
        subdir = create_mock_path("subdir", is_dir=True)
        file2 = create_mock_path("file2.md")

        with patch.object(Path, "exists", return_value=True):
            with patch.object(Path, "iterdir", side_effect=[[file1, subdir], [file2]]):
                result = markdown_service.get_content_tree()

                # Sorting logic puts directories first (not x.is_dir())
                assert len(result) == 2
                assert result[0]["name"] == "subdir"  # Directory first
                assert result[0]["type"] == "directory"
                assert len(result[0]["children"]) == 1
                assert result[0]["children"][0]["name"] == "file2.md"

                assert result[1]["name"] == "file1.md"  # File second
