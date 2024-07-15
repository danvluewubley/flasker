"""empty message

Revision ID: 996f0235e310
Revises: 19bfced61867
Create Date: 2024-07-14 17:26:42.860670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '996f0235e310'
down_revision = '19bfced61867'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=200), nullable=False))
        batch_op.create_unique_constraint(None, ['password'])

    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('password')

    # ### end Alembic commands ###

