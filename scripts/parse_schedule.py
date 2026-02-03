"""
Universal Schedule Parser for Salesforce Admin Platform

Parses schedules/sprintN_schedule.md files and extracts:
- Sprint metadata (number, dates, description)
- Tasks (title, category, deadline)

Author: AI Agent (Gemini)
Date: 2026-02-02
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class ScheduleParser:
    """Parser for sprint schedule Markdown files"""

    # Regex patterns
    TITLE_PATTERN = re.compile(r"^#\s+Cronograma\s+Sprint\s+(\d+)", re.IGNORECASE)
    DURATION_PATTERN = re.compile(
        r"\*\*Duración Total\*\*:\s*(\d+)\s+Semanas?\s*\((.+?)\)"
    )
    WEEK_PATTERN = re.compile(r"^##\s+Semana\s+(\d+)", re.IGNORECASE)
    DEADLINE_PATTERN = re.compile(
        r"\*\*Deadline para estar al día\*\*:\s*(\d+)\s+de\s+(\w+)", re.IGNORECASE
    )
    TASK_ROW_PATTERN = re.compile(
        r"^\|\s*\[([x\s])\]\s*\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|"
    )

    # Month mapping (Spanish to number)
    MONTHS = {
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12,
    }

    def __init__(self, schedule_path: str):
        """
        Initialize parser with schedule file path

        Args:
            schedule_path: Path to sprint schedule markdown file
        """
        self.schedule_path = Path(schedule_path)
        if not self.schedule_path.exists():
            raise FileNotFoundError(f"Schedule file not found: {schedule_path}")

        self.content = self.schedule_path.read_text(encoding="utf-8")
        self.lines = self.content.split("\n")

    def parse(self) -> Dict:
        """
        Parse schedule file and extract sprint data

        Returns:
            Dict with sprint metadata and tasks
        """
        sprint_data = {
            "number": None,
            "name": None,
            "description": None,
            "start_date": None,
            "end_date": None,
            "tasks": [],
        }

        current_week = None
        week_deadline = None

        for line in self.lines:
            # Extract sprint number and title
            title_match = self.TITLE_PATTERN.match(line)
            if title_match:
                sprint_data["number"] = int(title_match.group(1))
                sprint_data["name"] = f"Sprint {sprint_data['number']}"
                continue

            # Extract duration and dates
            duration_match = self.DURATION_PATTERN.search(line)
            if duration_match:
                date_range = duration_match.group(2)
                # Parse "5 de Enero - 6 de Febrero aprox"
                dates = self._parse_date_range(date_range)
                if dates:
                    sprint_data["start_date"] = dates[0]
                    sprint_data["end_date"] = dates[1]
                continue

            # Extract objective as description
            if line.startswith("**Objetivo**:"):
                sprint_data["description"] = line.replace("**Objetivo**:", "").strip()
                continue

            # Track current week
            week_match = self.WEEK_PATTERN.match(line)
            if week_match:
                current_week = int(week_match.group(1))
                week_deadline = None
                continue

            # Extract week deadline
            deadline_match = self.DEADLINE_PATTERN.search(line)
            if deadline_match and current_week:
                day = int(deadline_match.group(1))
                month_name = deadline_match.group(2).lower()
                month = self.MONTHS.get(month_name)
                if month:
                    # Assume year from sprint start date
                    year = (
                        sprint_data["start_date"].year
                        if sprint_data["start_date"]
                        else 2026
                    )
                    week_deadline = datetime(year, month, day)
                continue

            # Extract task rows
            task_match = self.TASK_ROW_PATTERN.match(line)
            if task_match and current_week:
                completed = task_match.group(1).strip().lower() == "x"
                date_str = task_match.group(2).strip()
                title = task_match.group(3).strip()
                category = task_match.group(4).strip()
                deadline_str = task_match.group(5).strip()

                # Parse specific deadline
                task_deadline = self._parse_deadline(deadline_str, sprint_data)

                # Determine markdown path based on category and title
                markdown_path = self._infer_markdown_path(
                    sprint_data["number"], title, category
                )

                task_data = {
                    "title": title,
                    "category": self._normalize_category(category),
                    "markdown_path": markdown_path,
                    "due_date": task_deadline or week_deadline,
                    "week": current_week,
                    "completed": completed,
                }

                sprint_data["tasks"].append(task_data)

        return sprint_data

    def _parse_date_range(self, date_range: str) -> Optional[List[datetime]]:
        """
        Parse date range string like "5 de Enero - 6 de Febrero aprox"

        Args:
            date_range: Date range string

        Returns:
            List of [start_date, end_date] or None
        """
        # Remove "aprox" and extra spaces
        date_range = date_range.replace("aprox", "").strip()

        # Split by dash
        parts = date_range.split("-")
        if len(parts) != 2:
            return None

        start_str = parts[0].strip()
        end_str = parts[1].strip()

        # Parse each date
        start_date = self._parse_spanish_date(start_str)
        end_date = self._parse_spanish_date(end_str)

        if start_date and end_date:
            return [start_date, end_date]

        return None

    def _parse_spanish_date(self, date_str: str) -> Optional[datetime]:
        """
        Parse Spanish date like "5 de Enero" or "6 de Febrero"

        Args:
            date_str: Spanish date string

        Returns:
            datetime object or None
        """
        # Pattern: "5 de Enero" or "6 de Febrero"
        match = re.match(r"(\d+)\s+de\s+(\w+)", date_str, re.IGNORECASE)
        if not match:
            return None

        day = int(match.group(1))
        month_name = match.group(2).lower()
        month = self.MONTHS.get(month_name)

        if not month:
            return None

        # Assume current year or 2026
        year = 2026

        try:
            return datetime(year, month, day)
        except ValueError:
            return None

    def _parse_deadline(
        self, deadline_str: str, sprint_data: Dict
    ) -> Optional[datetime]:
        """
        Parse deadline string like "9 de Enero"

        Args:
            deadline_str: Deadline string
            sprint_data: Sprint data for year context

        Returns:
            datetime object or None
        """
        return self._parse_spanish_date(deadline_str)

    def _normalize_category(self, category: str) -> str:
        """
        Normalize category name to match database enum

        Args:
            category: Raw category from markdown

        Returns:
            Normalized category (Teoria, Practica, Superbadge)
        """
        category_lower = category.lower().strip()

        if "teoria" in category_lower or "teoría" in category_lower:
            return "Teoria"
        elif "practica" in category_lower or "práctica" in category_lower:
            return "Practica"
        elif "superbadge" in category_lower or "formulario" in category_lower:
            return "Superbadge"
        else:
            # Default to Teoria if unknown
            return "Teoria"

    def _infer_markdown_path(
        self, sprint_number: int, title: str, category: str
    ) -> str:
        """
        Infer markdown file path based on sprint, title, and category

        Args:
            sprint_number: Sprint number
            title: Task title
            category: Task category

        Returns:
            Relative path to markdown file
        """
        # Normalize category
        normalized_category = self._normalize_category(category)

        # For Superbadges, use Superbadges folder
        if normalized_category == "Superbadge":
            # Extract superbadge name from title
            if "Object" in title or "Relationship" in title:
                return "Superbadges/Object_Relationship.md"
            elif "Data Import" in title:
                return "Superbadges/Data_Import.md"
            elif "Formula" in title or "Fórmula" in title:
                return "Superbadges/Formula_Fields.md"
            elif "Seguridad" in title and "Data Import" in title:
                # "SB - Seguridad o Data Import" -> use Data Import
                return "Superbadges/Data_Import.md"
            elif "Seguridad" in title or "Security" in title:
                return "Superbadges/Security.md"
            elif "General" in title:
                return "Superbadges/General.md"
            else:
                # Generic superbadge - use sanitized title
                filename = (
                    title.lower()
                    .replace(" ", "_")
                    .replace("á", "a")
                    .replace("ó", "o")
                    .replace("é", "e")
                    .replace("í", "i")
                    .replace("ú", "u")
                )
                filename = re.sub(r"[^a-z0-9_]", "", filename)
                return f"Superbadges/{filename}.md"

        # For curriculum tasks, use curriculum/sprint_XX folder
        # This is a simplified mapping - can be enhanced later
        sprint_folder = f"curriculum/sprint_{sprint_number:02d}"

        # Generate a generic filename based on title
        # This can be improved with a mapping file later
        filename = (
            title.lower()
            .replace(" ", "_")
            .replace("á", "a")
            .replace("ó", "o")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ú", "u")
        )
        filename = re.sub(r"[^a-z0-9_]", "", filename)

        return f"{sprint_folder}/{filename}.md"


def parse_schedule_file(schedule_path: str) -> Dict:
    """
    Convenience function to parse a schedule file

    Args:
        schedule_path: Path to schedule markdown file

    Returns:
        Dict with sprint data and tasks
    """
    parser = ScheduleParser(schedule_path)
    return parser.parse()


if __name__ == "__main__":
    # Test parser with Sprint 1
    import json

    schedule_path = "schedules/sprint1_schedule.md"
    sprint_data = parse_schedule_file(schedule_path)

    print("=" * 80)
    print("SPRINT DATA PARSED")
    print("=" * 80)
    print(json.dumps(sprint_data, indent=2, default=str))
    print("=" * 80)
    print(f"Sprint {sprint_data['number']}: {sprint_data['name']}")
    print(f"Start: {sprint_data['start_date']}")
    print(f"End: {sprint_data['end_date']}")
    print(f"Tasks: {len(sprint_data['tasks'])}")
    print("=" * 80)
