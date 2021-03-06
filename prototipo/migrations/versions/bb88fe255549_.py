"""empty message

Revision ID: bb88fe255549
Revises: 175235720f56
Create Date: 2020-12-15 20:37:21.871157

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'bb88fe255549'
down_revision = '175235720f56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensor_tipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=255), nullable=False),
    sa.Column('descricao', sa.String(length=255), nullable=False),
    sa.Column('params', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('codigo')
    )
    op.add_column('sensor', sa.Column('tipo_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'sensor', 'sensor_tipo', ['tipo_id'], ['id'])
    op.drop_column('sensor', 'tipo')
    op.drop_column('sensor', 'params')
    op.drop_column('sensor', 'descricao')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sensor', sa.Column('descricao', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('sensor', sa.Column('params', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('sensor', sa.Column('tipo', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'sensor', type_='foreignkey')
    op.drop_column('sensor', 'tipo_id')
    op.drop_table('sensor_tipo')
    # ### end Alembic commands ###
