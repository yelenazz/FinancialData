"""Added Ticker Models

Revision ID: 00db96ed24b0
Revises: a500e5a11d6f
Create Date: 2018-05-14 14:07:27.430040

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '00db96ed24b0'
down_revision = 'a500e5a11d6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tickers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('history', sa.Column('ticker_id', sa.Integer(), nullable=False))
    op.alter_column('history', 'date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.create_foreign_key(None, 'history', 'tickers', ['ticker_id'], ['id'], ondelete='CASCADE')
    op.add_column('insiders', sa.Column('ticker_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'insiders', 'tickers', ['ticker_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'insiders', type_='foreignkey')
    op.drop_column('insiders', 'ticker_id')
    op.drop_constraint(None, 'history', type_='foreignkey')
    op.alter_column('history', 'date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('history', 'ticker_id')
    op.drop_table('tickers')
    # ### end Alembic commands ###
