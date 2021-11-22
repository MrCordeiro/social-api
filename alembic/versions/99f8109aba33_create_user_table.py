"""Create user table

Revision ID: 99f8109aba33
Revises: b51a6967285d
Create Date: 2021-11-22 14:36:32.936080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "99f8109aba33"
down_revision = "b51a6967285d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("users")
