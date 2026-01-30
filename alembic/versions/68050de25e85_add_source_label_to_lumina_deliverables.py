"""add source_label to lumina_deliverables

Revision ID: 68050de25e85
Revises: 39117a717014
Create Date: 2026-01-30 09:20:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68050de25e85'
down_revision = '39117a717014'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('lumina_deliverables', sa.Column('source_label', sa.String(), nullable=True))


def downgrade():
    op.drop_column('lumina_deliverables', 'source_label')
