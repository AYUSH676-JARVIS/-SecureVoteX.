from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.auth import (
    get_current_admin,
    get_current_user,
)
from app.models.user import User
from app.schemas.election import (
    ElectionCreate,
    ElectionResponse,
    ElectionUpdate,
)
from app.services.election_service import ElectionService

router = APIRouter(
    prefix="/elections",
    tags=["Elections"],
)


@router.post(
    "/",
    response_model=ElectionResponse,
    status_code=201,
)
def create_election(
    request: ElectionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
):
    try:
        return ElectionService.create(
            db=db,
            request=request,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[ElectionResponse],
)
def get_elections(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ElectionService.get_all(db)


@router.get(
    "/{election_id}",
    response_model=ElectionResponse,
)
def get_election(
    election_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return ElectionService.get_by_id(
            db,
            election_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.put(
    "/{election_id}",
    response_model=ElectionResponse,
)
def update_election(
    election_id: str,
    request: ElectionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
):
    try:
        return ElectionService.update(
            db,
            election_id,
            request,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.delete(
    "/{election_id}",
)
def delete_election(
    election_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
):
    try:
        return ElectionService.delete(
            db,
            election_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )