"""create phone nuber for user column

Revision ID: 1f9e423fc1b6
Revises: 
Create Date: 2024-06-22 19:41:49.071223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f9e423fc1b6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(20), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
