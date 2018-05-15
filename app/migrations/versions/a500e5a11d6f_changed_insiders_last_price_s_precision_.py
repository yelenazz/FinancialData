"""Changed insiders.last_price's precision to 4

Revision ID: a500e5a11d6f
Revises: a5102c498de7
Create Date: 2018-05-14 11:55:11.325425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a500e5a11d6f'
down_revision = 'a5102c498de7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('insiders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('inner_id', sa.Integer(), nullable=True),
    sa.Column('relation', sa.String(length=100), nullable=True),
    sa.Column('last_date', sa.DateTime(), nullable=True),
    sa.Column('transaction_type', sa.String(length=100), nullable=True),
    sa.Column('owner_type', sa.String(length=20), nullable=True),
    sa.Column('shares_traded', sa.Integer(), nullable=True),
    sa.Column('last_price', sa.Float(precision=4), nullable=True),
    sa.Column('shares_held', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('insiders')
    # ### end Alembic commands ###
