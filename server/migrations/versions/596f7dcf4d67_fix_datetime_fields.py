"""Fix datetime fields

Revision ID: 596f7dcf4d67
Revises: 5cbeeb4f2fdd
Create Date: 2024-10-17 06:24:52.323844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '596f7dcf4d67'
down_revision = '5cbeeb4f2fdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('body', sa.String(), nullable=False))
    op.add_column('messages', sa.Column('username', sa.String(), nullable=False))
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('messages', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'updated_at')
    op.drop_column('messages', 'created_at')
    op.drop_column('messages', 'username')
    op.drop_column('messages', 'body')
    # ### end Alembic commands ###
