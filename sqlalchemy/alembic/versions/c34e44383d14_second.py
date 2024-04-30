"""second

Revision ID: c34e44383d14
Revises: 73b0022e760c
Create Date: 2024-04-16 10:48:18.748448

"""
from alembic import op
import sqlalchemy as sa
from infra.repository.filmes_repository import FilmesRepository


# revision identifiers, used by Alembic.
revision = 'c34e44383d14'
down_revision = '73b0022e760c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    filmes_repository = FilmesRepository()
    filmes_repository.insert('Ola', 'Mundo', 123)


def downgrade() -> None:
    filmes_repository = FilmesRepository()
    filmes_repository.delete('Ola')
