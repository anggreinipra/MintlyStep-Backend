"""create transactions table

Revision ID: b49b84a7d589
Revises: 59c1db0e7147
Create Date: 2025-06-30 17:12:58.577717

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b49b84a7d589'
down_revision: Union[str, None] = '59c1db0e7147'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
