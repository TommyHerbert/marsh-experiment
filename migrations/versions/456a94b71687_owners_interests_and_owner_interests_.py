"""owners, interests and owner_interests tables

Revision ID: 456a94b71687
Revises: 
Create Date: 2019-10-30 12:26:27.035585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '456a94b71687'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('mobile', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owner_interest',
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('interest_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['interest_id'], ['interest.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], ),
    sa.PrimaryKeyConstraint('owner_id', 'interest_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owner_interest')
    op.drop_table('owner')
    op.drop_table('interest')
    # ### end Alembic commands ###
