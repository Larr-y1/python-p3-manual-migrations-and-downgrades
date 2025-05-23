"""Renaming birthday column to date of birth

Revision ID: 133f6a21f130
Revises: 7384df17b86f
Create Date: 2025-05-23 14:11:30.405787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '133f6a21f130'
down_revision = '7384df17b86f'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('students', 'birthday', new_column_name='date_of_birth')


def downgrade():
    op.alter_column('students', 'date_of_birth', new_column_name='birthday')