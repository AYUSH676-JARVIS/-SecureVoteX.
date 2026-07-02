import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    full_name: Mapped[str] = mapped_column(String(120), nullable=False)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    role_id: Mapped[str] = mapped_column(
        ForeignKey("roles.id"),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)

    failed_login_attempts: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    last_login: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    role = relationship("Role")