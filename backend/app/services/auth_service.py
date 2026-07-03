from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.role_repository import RoleRepository
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest


class AuthService:

    @staticmethod
    def register(db: Session, request: RegisterRequest):

        existing = UserRepository.get_by_email(
            db,
            request.email,
        )

        if existing:
            raise ValueError("Email already exists")

        voter_role = RoleRepository.get_by_name(db, "VOTER")

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

        return UserRepository.create(db, user)