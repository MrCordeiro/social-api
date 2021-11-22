"""Add owner FK to posts

Revision ID: 9375f9ce7b47
Revises: 99f8109aba33
Create Date: 2021-11-22 14:38:41.586401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9375f9ce7b47"
down_revision = "99f8109aba33"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
