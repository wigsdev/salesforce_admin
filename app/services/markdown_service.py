"""
Markdown service for reading and rendering markdown files.
"""

from pathlib import Path
from typing import Optional, Dict, List
import markdown

from app.config import settings


class MarkdownService:
    """Service for reading and rendering markdown files."""

    def __init__(self):
        """Initialize the markdown service."""
        self.content_path = Path(settings.CONTENT_PATH)
        self.md = markdown.Markdown(
            extensions=[
                "tables",
                "fenced_code",
                "codehilite",
                "toc",
                "nl2br",
                "sane_lists",
            ],
            extension_configs={
                "codehilite": {"css_class": "highlight", "linenums": False}
            },
        )

    def get_file_path(self, relative_path: str) -> Optional[Path]:
        """
        Get the absolute path to a markdown file.

        Args:
            relative_path: Relative path from content directory

        Returns:
            Absolute path if file exists, None otherwise
        """
        # Remove leading slash if present
        if relative_path.startswith("/"):
            relative_path = relative_path[1:]

        # Construct full path
        full_path = self.content_path / relative_path

        # Add .md extension if not present
        if not full_path.suffix:
            full_path = full_path.with_suffix(".md")

        # Check if file exists
        if full_path.exists() and full_path.is_file():
            return full_path

        return None

    def read_markdown(self, relative_path: str) -> Optional[str]:
        """
        Read markdown file content.

        Args:
            relative_path: Relative path from content directory

        Returns:
            Markdown content as string, None if file not found
        """
        file_path = self.get_file_path(relative_path)

        if not file_path:
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return None

    def render_markdown(self, content: str) -> str:
        """
        Convert markdown to HTML.

        Args:
            content: Markdown content

        Returns:
            HTML content
        """
        # Reset the markdown instance for fresh conversion
        self.md.reset()
        return self.md.convert(content)

    def get_document(self, relative_path: str) -> Optional[Dict[str, str]]:
        """
        Get a markdown document with metadata.

        Args:
            relative_path: Relative path from content directory

        Returns:
            Dictionary with 'content', 'html', 'toc', 'title'
        """
        md_content = self.read_markdown(relative_path)

        if not md_content:
            return None

        html_content = self.render_markdown(md_content)

        # Extract title from first h1 or use filename
        title = self._extract_title(md_content, relative_path)

        return {
            "content": md_content,
            "html": html_content,
            "toc": self.md.toc if hasattr(self.md, "toc") else "",
            "title": title,
            "path": relative_path,
        }

    def _extract_title(self, content: str, fallback_path: str) -> str:
        """
        Extract title from markdown content.

        Args:
            content: Markdown content
            fallback_path: Path to use as fallback

        Returns:
            Document title
        """
        lines = content.split("\n")
        for line in lines:
            if line.strip().startswith("# "):
                return line.strip()[2:].strip()

        # Fallback to filename
        return Path(fallback_path).stem.replace("_", " ").replace("-", " ").title()

    def list_directory(self, relative_path: str = "") -> List[Dict[str, str]]:
        """
        List markdown files in a directory.

        Args:
            relative_path: Relative path from content directory

        Returns:
            List of dictionaries with file info
        """
        if relative_path.startswith("/"):
            relative_path = relative_path[1:]

        dir_path = (
            self.content_path / relative_path if relative_path else self.content_path
        )

        if not dir_path.exists() or not dir_path.is_dir():
            return []

        files = []
        for item in sorted(dir_path.iterdir()):
            if item.is_file() and item.suffix == ".md":
                files.append(
                    {
                        "name": item.stem,
                        "path": str(item.relative_to(self.content_path)),
                        "type": "file",
                    }
                )
            elif item.is_dir() and not item.name.startswith("."):
                files.append(
                    {
                        "name": item.name,
                        "path": str(item.relative_to(self.content_path)),
                        "type": "directory",
                    }
                )

        return files
