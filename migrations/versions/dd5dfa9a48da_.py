"""empty message

Revision ID: dd5dfa9a48da
Revises: 1387c836c1b6
Create Date: 2021-12-15 06:33:45.021412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd5dfa9a48da'
down_revision = '1387c836c1b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('date_created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('company', 'date_created')
    # ### end Alembic commands ###
