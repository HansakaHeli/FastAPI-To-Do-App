"""create address_id to users

Revision ID: 15d6cd988839
Revises: e9c576d1debd
Create Date: 2024-06-22 20:24:16.408815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15d6cd988839'
down_revision: Union[str, None] = 'e9c576d1debd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table="users", referent_table="address", local_cols=['address_id'], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column('users', 'address_id')
