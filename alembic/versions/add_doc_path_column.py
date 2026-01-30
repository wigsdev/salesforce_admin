"""add doc_path to lumina_tasks

Revision ID: add_doc_path_column
Revises: 20260128_cleanup_lumina
Create Date: 2026-01-30 02:25:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "add_doc_path_column"
down_revision = "20260128_cleanup"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("lumina_tasks", sa.Column("doc_path", sa.String(), nullable=True))


def downgrade():
    op.drop_column("lumina_tasks", "doc_path")
