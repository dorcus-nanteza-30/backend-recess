"""Migrating user,ticket,squad,teamstatistics,orderitem,order,merchandise,membership,event,donation,contact.

Revision ID: de1d6128873c
Revises: 
Create Date: 2024-07-02 18:36:30.663721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de1d6128873c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('merchandises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('category', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('squads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.String(length=50), nullable=False),
    sa.Column('jersey_number', sa.String(length=30), nullable=False),
    sa.Column('biography', sa.String(length=255), nullable=False),
    sa.Column('image', sa.Text(), nullable=False),
    sa.Column('weight', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('height', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('jersey_number')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('contact', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('join_date', sa.DateTime(), nullable=False),
    sa.Column('membership_status', sa.String(length=50), nullable=False),
    sa.Column('user_type', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contact'),
    sa.UniqueConstraint('email')
    )
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('message', sa.String(length=255), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('donations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('donation_date', sa.DateTime(), nullable=False),
    sa.Column('message', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('memberships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('membership_type', sa.String(length=50), nullable=False),
    sa.Column('age_group', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('status_of_order', sa.String(length=30), nullable=False),
    sa.Column('address_of_delivery', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('playerstatistics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('squad_id', sa.Integer(), nullable=False),
    sa.Column('matches_played', sa.Integer(), nullable=False),
    sa.Column('tries_scored', sa.Integer(), nullable=False),
    sa.Column('conversions', sa.Integer(), nullable=False),
    sa.Column('penalties', sa.Integer(), nullable=False),
    sa.Column('yellow_cards', sa.Integer(), nullable=False),
    sa.Column('red_cards', sa.Integer(), nullable=False),
    sa.Column('minutes_played', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['squad_id'], ['squads.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('section', sa.String(length=50), nullable=False),
    sa.Column('row', sa.String(length=50), nullable=False),
    sa.Column('seat', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('merchandise_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price_of_item', sa.Float(), nullable=False),
    sa.Column('total_amount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['merchandise_id'], ['merchandises.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('tickets')
    op.drop_table('playerstatistics')
    op.drop_table('orders')
    op.drop_table('memberships')
    op.drop_table('donations')
    op.drop_table('contacts')
    op.drop_table('users')
    op.drop_table('squads')
    op.drop_table('merchandises')
    op.drop_table('events')
    # ### end Alembic commands ###
