"""first

Revision ID: 73b0022e760c
Revises: 
Create Date: 2024-04-16 10:31:46.776085

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '73b0022e760c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'accont',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade() -> None:
    op.drop_table('account')
