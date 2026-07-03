from sqlalchemy.orm import Session

from app.models.election import Election
from app.repositories.election_repository import ElectionRepository
from app.schemas.election import (
    ElectionCreate,
    ElectionUpdate,
)


class ElectionService:

    @staticmethod
    def create(
        db: Session,
        request: ElectionCreate,
    ):

        if request.end_date <= request.start_date:
            raise ValueError(
                "End date must be after start date"
            )

        election = Election(
            title=request.title,
            description=request.description,
            start_date=request.start_date,
            end_date=request.end_date,
            is_active=False,
            is_completed=False,
        )

        return ElectionRepository.create(
            db,
            election,
        )

    @staticmethod
    def get_all(
        db: Session,
    ):
        return ElectionRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db: Session,
        election_id: str,
    ):
        election = ElectionRepository.get_by_id(
            db,
            election_id,
        )

        if election is None:
            raise ValueError("Election not found")

        return election

    @staticmethod
    def update(
        db: Session,
        election_id: str,
        request: ElectionUpdate,
    ):
        election = ElectionRepository.get_by_id(
            db,
            election_id,
        )

        if election is None:
            raise ValueError("Election not found")

        if request.end_date <= request.start_date:
            raise ValueError(
                "End date must be after start date"
            )

        election.title = request.title
        election.description = request.description
        election.start_date = request.start_date
        election.end_date = request.end_date
        election.is_active = request.is_active
        election.is_completed = request.is_completed

        return ElectionRepository.update(
            db,
            election,
        )

    @staticmethod
    def delete(
        db: Session,
        election_id: str,
    ):
        election = ElectionRepository.get_by_id(
            db,
            election_id,
        )

        if election is None:
            raise ValueError("Election not found")

        ElectionRepository.delete(
            db,
            election,
        )

        return {
            "message": "Election deleted successfully"
        }