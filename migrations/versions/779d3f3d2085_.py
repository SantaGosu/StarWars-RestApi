"""empty message

Revision ID: 779d3f3d2085
Revises: d2cbdba16124
Create Date: 2022-10-01 22:02:15.724118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '779d3f3d2085'
down_revision = 'd2cbdba16124'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('climate', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planets', 'climate')
    # ### end Alembic commands ###
