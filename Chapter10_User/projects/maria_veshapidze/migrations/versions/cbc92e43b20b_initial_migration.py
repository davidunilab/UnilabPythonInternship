"""initial migration

Revision ID: cbc92e43b20b
Revises: 
Create Date: 2021-04-20 23:35:17.587945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbc92e43b20b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tutors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.Column('subject', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tutors_email'), 'tutors', ['email'], unique=True)
    op.create_index(op.f('ix_tutors_username'), 'tutors', ['username'], unique=True)
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.Column('tutor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tutor_id'], ['tutors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_students_email'), 'students', ['email'], unique=True)
    op.create_index(op.f('ix_students_username'), 'students', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_username'), table_name='students')
    op.drop_index(op.f('ix_students_email'), table_name='students')
    op.drop_table('students')
    op.drop_index(op.f('ix_tutors_username'), table_name='tutors')
    op.drop_index(op.f('ix_tutors_email'), table_name='tutors')
    op.drop_table('tutors')
    # ### end Alembic commands ###
