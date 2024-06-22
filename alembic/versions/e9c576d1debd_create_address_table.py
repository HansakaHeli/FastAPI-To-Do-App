"""create address table

Revision ID: e9c576d1debd
Revises: 1f9e423fc1b6
Create Date: 2024-06-22 20:16:25.161126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9c576d1debd'
down_revision: Union[str, None] = '1f9e423fc1b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
