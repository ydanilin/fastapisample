from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from app.api.utils.db import get_db
from app.api.utils.security import get_current_user
from app.core import config
from app.core.jwt import create_access_token
from app.models.token import Token
from app import crud

router = APIRouter()

security = HTTPBasic()


@router.post("/token", response_model=Token, tags=["login"])
def login_access_token(
    db: Session = Depends(get_db),
    credentials: HTTPBasicCredentials = Depends(security)
):
    user = crud.user.authenticate(
        db, email=credentials.username, password=credentials.password
    )
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect email or password"
        )
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    token = create_access_token(
        data={"user_id": user.id, "user_email": user.email},
        expires_delta=access_token_expires
    )
    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_in": config.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }


# @router.post("/login/test-token", tags=["login"], response_model=User)
@router.post("/test-token", tags=["login"])
# def test_token(current_user: DBUser = Depends(get_current_user)):
def test_token(current_user=Depends(get_current_user)):
    """
    Test access token
    """
    return current_user
