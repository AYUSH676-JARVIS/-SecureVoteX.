from datetime import datetime

from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.role_repository import RoleRepository
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, RegisterRequest


class AuthService:

    @staticmethod
    def register(db: Session, request: RegisterRequest):

        existing = UserRepository.get_by_email(
            db,
            request.email,
        )

        if existing:
            raise ValueError("Email already exists")

        voter_role = RoleRepository.get_by_name(
            db,
            "VOTER",
        )

        if voter_role is None:
            raise ValueError("VOTER role not found")

        user = User(
            full_name=request.full_name,
            email=request.email,
            password_hash=hash_password(request.password),
            role_id=voter_role.id,
            is_active=True,
            is_verified=False,
        )

        return UserRepository.create(
            db,
            user,
        )

    @staticmethod
    def login(db: Session, request: LoginRequest):

        user = UserRepository.get_by_email(
            db,
            request.email,
        )

        if user is None:
            raise ValueError("Invalid email or password")

        if not verify_password(
            request.password,
            user.password_hash,
        ):
            UserRepository.increment_failed_attempts(
                db,
                user,
            )

            raise ValueError("Invalid email or password")

        user.failed_login_attempts = 0
        user.last_login = datetime.utcnow()

        UserRepository.update(
            db,
            user,
        )

        access_token = create_access_token(
            user.email,
        )

        refresh_token = create_refresh_token(
            user.email,
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }