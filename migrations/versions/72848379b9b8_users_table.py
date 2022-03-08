"""users table

Revision ID: 72848379b9b8
Revises: dd29696af9c5
Create Date: 2022-03-04 09:11:39.574409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72848379b9b8'
down_revision = 'dd29696af9c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('todo', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'todo')
    # ### end Alembic commands ###
