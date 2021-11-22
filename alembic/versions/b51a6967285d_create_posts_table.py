"""Create posts table

Revision ID: b51a6967285d
Revises: 
Create Date: 2021-11-21 14:26:12.673663

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision = "b51a6967285d"
down_revision = None
branch_labels = None
depends_on = None


# Runs the commands from running the migration we want
def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("published", sa.Boolean(), nullable=False, default=True),
        sa.Column(
            "created_at", sa.DateTime(), nullable=False, server_default=text("now()")
        ),
    )


# Runs the logic to revert the migration
def downgrade():
    op.drop_table("posts")
