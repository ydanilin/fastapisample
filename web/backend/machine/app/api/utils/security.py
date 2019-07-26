import jwt
from jwt import PyJWTError
from fastapi import Depends, HTTPException, Security
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN

from fastapi.security import OAuth2PasswordBearer
from app.api.utils.db import get_db
from app.core import config
from app.core.jwt import ALGORITHM
from app.models.token import TokenPayload
from app import crud


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{config.API_V1_STR}/oauth/token"
)


def get_current_user(
    db: Session = Depends(get_db), token: str = Security(reusable_oauth2)
):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )
    user = crud.user.get(db, user_id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
