"""create auth tables

Revision ID: auth_tables_20241106
Revises: e5d6103b8bca
Create Date: 2024-11-06 10:00:00.000000

"""
from datetime import timezone
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'auth_tables_20241106'
down_revision = 'e5d6103b8bca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add new columns to users table
    op.add_column('users', sa.Column('email_verified', sa.Boolean(), nullable=False, server_default='false'))
    op.add_column('users', sa.Column('apple_id', sa.String(), nullable=True, unique=True))

    # Create user_auth_providers table
    op.create_table(
        'user_auth_providers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('provider', sa.Enum('GOOGLE', 'APPLE', 'EMAIL', name='authprovidertype'), nullable=False),
        sa.Column('provider_user_id', sa.String(255), nullable=False),
        sa.Column('provider_email', sa.String(255), nullable=False),
        sa.Column('access_token', sa.String(1024)),
        sa.Column('refresh_token', sa.String(1024)),
        sa.Column('token_expires_at', sa.DateTime(timezone=True)),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, 
                 server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False,
                 server_default=sa.text('CURRENT_TIMESTAMP'),
                 server_onupdate=sa.text('CURRENT_TIMESTAMP')),
        sa.UniqueConstraint('provider', 'provider_user_id')
    )

    # Create user_sessions table
    op.create_table(
        'user_sessions',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('refresh_token', sa.String(1024), unique=True, nullable=False),
        sa.Column('device_id', sa.String(255)),
        sa.Column('platform', sa.Enum('WEB', 'IOS', 'ANDROID', name='platformtype')),
        sa.Column('ip_address', sa.String(45)),
        sa.Column('user_agent', sa.String(512)),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False,
                 server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('last_used_at', sa.DateTime(timezone=True), nullable=False,
                 server_default=sa.text('CURRENT_TIMESTAMP'),
                 server_onupdate=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true')
    )

    # Create indexes for better query performance
    op.create_index('idx_user_auth_providers_user_id', 'user_auth_providers', ['user_id'])
    op.create_index('idx_user_sessions_user_id', 'user_sessions', ['user_id'])
    op.create_index('idx_user_sessions_refresh_token', 'user_sessions', ['refresh_token'])


def downgrade() -> None:
    # Drop indexes
    op.drop_index('idx_user_sessions_refresh_token')
    op.drop_index('idx_user_sessions_user_id')
    op.drop_index('idx_user_auth_providers_user_id')

    # Drop tables
    op.drop_table('user_sessions')
    op.drop_table('user_auth_providers')

    # Drop enum types
    op.execute('DROP TYPE platformtype')
    op.execute('DROP TYPE authprovidertype')

    # Remove columns from users table
    op.drop_column('users', 'apple_id')
    op.drop_column('users', 'email_verified')