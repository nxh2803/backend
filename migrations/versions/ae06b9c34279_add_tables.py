"""add tables

Revision ID: ae06b9c34279
Revises: 9b12af01f82f
Create Date: 2023-07-01 16:11:36.860184

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ae06b9c34279'
down_revision = '9b12af01f82f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invoice', sa.Column('total_amount', sa.Float(), nullable=True))
    op.drop_column('order', 'total_amount')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('total_amount', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.drop_column('invoice', 'total_amount')
    # ### end Alembic commands ###
