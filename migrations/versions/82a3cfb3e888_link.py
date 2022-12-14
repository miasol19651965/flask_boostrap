"""link

Revision ID: 82a3cfb3e888
Revises: 05d284c7258c
Create Date: 2022-12-14 10:00:22.653858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82a3cfb3e888'
down_revision = '05d284c7258c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('link', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('link')
        batch_op.drop_column('price')

    # ### end Alembic commands ###
