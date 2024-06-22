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
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(20), nullable=False),
                    sa.Column('address2', sa.String(20), nullable=False),
                    sa.Column('city', sa.String(20), nullable=False),
                    sa.Column('country', sa.String(20), nullable=False),
                    sa.Column('postalcode', sa.String(20), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('address')
