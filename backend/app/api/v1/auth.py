from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.auth import RegisterRequest, UserResponse
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)
@router.post(

    "/register",

    response_model=UserResponse,

    status_code=201,

)

def register(

    request: RegisterRequest,

    db: Session = Depends(get_db),

):

    try:

        user = AuthService.register(

            db=db,

            request=request,

        )

        return user

    except ValueError as e:

        raise HTTPException(

            status_code=400,

            detail=str(e),

        )