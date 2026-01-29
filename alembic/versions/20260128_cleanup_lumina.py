"""Refactor and clean Lumina model

Revision ID: 20260128_cleanup
Revises: 182f3ee31ba7
Create Date: 2026-01-28 23:55:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "20260128_cleanup"
down_revision: Union[str, None] = "182f3ee31ba7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Rename 'path' to 'reference'
    op.alter_column("lumina_deliverables", "path", new_column_name="reference")

    # 2. Drop 'role' and 'weight' columns
    op.drop_column("lumina_deliverables", "role")
    op.drop_column("lumina_deliverables", "weight")

    # 3. Fix constraints/indexes if necessary
    # Note: 'path' was unique and indexed. 'reference' should likely carry that over or be adjusted.
    # Postgres automatically renames indexes when columns are renamed usually, but let's be safe.
    # We'll trust the rename preserves the index, but let's drop the old specific indexes on role
    # op.drop_index('ix_lumina_deliverables_role', table_name='lumina_deliverables') # Handled by drop_column usually but explicit is good


def downgrade() -> None:
    # Reverse operations
    op.add_column(
        "lumina_deliverables",
        sa.Column(
            "weight",
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
            server_default="0",
        ),
    )
    op.add_column(
        "lumina_deliverables",
        sa.Column(
            "role",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            server_default="general",
        ),
    )

    op.alter_column("lumina_deliverables", "reference", new_column_name="path")
