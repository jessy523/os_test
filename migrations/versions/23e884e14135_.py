"""empty message

Revision ID: 23e884e14135
Revises: cefd1dab6d8c
Create Date: 2022-03-02 15:27:18.689889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23e884e14135'
down_revision = 'cefd1dab6d8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('scheduled_time', sa.DateTime(), nullable=False))
    op.drop_column('user', 'time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('time', sa.VARCHAR(length=120), nullable=False))
    op.drop_column('user', 'scheduled_time')
    # ### end Alembic commands ###