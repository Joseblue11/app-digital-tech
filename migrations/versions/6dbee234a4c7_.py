"""empty message

Revision ID: 6dbee234a4c7
Revises: 3c4bca2fb4b1
Create Date: 2024-08-06 08:14:29.741861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dbee234a4c7'
down_revision = '3c4bca2fb4b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('avatar', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('username', sa.String(length=30), nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=10),
               existing_nullable=False)
        batch_op.drop_constraint('user_email_key', type_='unique')
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('email')
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('user_email_key', ['email'])
        batch_op.alter_column('password',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.drop_column('username')
        batch_op.drop_column('last_name')
        batch_op.drop_column('name')
        batch_op.drop_column('avatar')

    # ### end Alembic commands ###