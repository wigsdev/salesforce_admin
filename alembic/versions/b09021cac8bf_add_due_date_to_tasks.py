"""add_due_date_to_tasks

Revision ID: b09021cac8bf
Revises: 790123abc456
Create Date: 2026-02-02 03:13:43.503711

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "b09021cac8bf"
down_revision: Union[str, None] = "790123abc456"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Check if column exists first to make it idempotent
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [c["name"] for c in inspector.get_columns("tasks")]

    if "due_date" not in columns:
        # Add due_date column to tasks table
        op.add_column("tasks", sa.Column("due_date", sa.DateTime(), nullable=True))


def downgrade() -> None:
    # Remove due_date column from tasks table
    op.drop_column("tasks", "due_date")
