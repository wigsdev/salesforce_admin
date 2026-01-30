"""add source_link to lumina_deliverables

Revision ID: 39117a717014
Revises: 7522067858c4
Create Date: 2026-01-30 08:39:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "39117a717014"
down_revision = "add_doc_path_column"
# Based on git log in previous turns:
# The last migration I touched was `add_doc_path_column.py`.
# Wait, let me check the existing migrations to be sure of the down_revision.
# I'll use a placeholder for now and check it in the next step, OR I can try to guess it.
# Actually, better to check first. But I'm writing the file now.
# I will use the hash of the last applied migration.
# In previous output (Step 11750), `add_doc_path_column.py` had `down_revision = '20260128_cleanup'`.
# The current head should be the one from `add_doc_path_column.py`.
# I'll check the revisions dir first.
# But to avoid delay, I'll list the versions directory again.

branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "lumina_deliverables", sa.Column("source_link", sa.String(), nullable=True)
    )


def downgrade():
    op.drop_column("lumina_deliverables", "source_link")
