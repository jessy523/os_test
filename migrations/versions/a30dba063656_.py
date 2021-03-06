"""empty message

Revision ID: a30dba063656
Revises: 8a4e1ad2d166
Create Date: 2022-03-03 08:23:33.229990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a30dba063656'
down_revision = '8a4e1ad2d166'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'title',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.drop_index('ix_user_title', table_name='user')
    op.create_index(op.f('ix_user_title'), 'user', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_title'), table_name='user')
    op.create_index('ix_user_title', 'user', ['title'], unique=False)
    op.alter_column('user', 'title',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###
