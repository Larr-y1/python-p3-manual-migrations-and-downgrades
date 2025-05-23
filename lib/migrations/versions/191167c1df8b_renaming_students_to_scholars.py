"""Renaming students to scholars

Revision ID: 191167c1df8b
Revises: 791279dd0760
Create Date: 2025-05-23 13:39:01.661240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '191167c1df8b'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
