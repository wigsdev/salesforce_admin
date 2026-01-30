"""drop unique constraint lumina reference

Revision ID: 790123abc456
Revises: 68050de25e85
Create Date: 2026-01-30 09:56:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '790123abc456'
down_revision = '68050de25e85'
branch_labels = None
depends_on = None


def upgrade():
    # Drop the unique index that causes issues with empty references
    op.drop_index('ix_lumina_deliverables_path', table_name='lumina_deliverables')
    # Optionally create a non-unique index if needed, but for now just dropping is enough to fix the error.


def downgrade():
    # Restore the unique index
    op.create_index('ix_lumina_deliverables_path', 'lumina_deliverables', ['reference'], unique=True)
