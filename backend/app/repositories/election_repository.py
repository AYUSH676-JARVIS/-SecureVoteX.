from sqlalchemy.orm import Session

from app.models.election import Election


class ElectionRepository:

    @staticmethod
    def create(db: Session, election: Election):
        db.add(election)
        db.commit()
        db.refresh(election)
        return election

    @staticmethod
    def get_all(db: Session):
        return db.query(Election).all()

    @staticmethod
    def get_by_id(db: Session, election_id: str):
        return (
            db.query(Election)
            .filter(Election.id == election_id)
            .first()
        )

    @staticmethod
    def update(db: Session, election: Election):
        db.commit()
        db.refresh(election)
        return election

    @staticmethod
    def delete(db: Session, election: Election):
        db.delete(election)
        db.commit()