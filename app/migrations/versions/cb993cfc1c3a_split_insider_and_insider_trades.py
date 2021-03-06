"""split insider and insider trades

Revision ID: cb993cfc1c3a
Revises: 31c40d9957b2
Create Date: 2018-05-18 12:18:26.087824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb993cfc1c3a'
down_revision = '31c40d9957b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('insider_trades', 'relation')
    op.add_column('insiders', sa.Column('relation', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('insiders', 'relation')
    op.add_column('insider_trades', sa.Column('relation', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
