import warnings
import uuid
import bcrypt
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import HTTPException, Header
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel
import dotenv
import os
from typing import Any

dotenv.load_dotenv()

# openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY")
if SECRET_KEY is None:
    raise Exception(
        "SECRET KEY could not be loaded. Did you forget to add an '.env' file?"
    )
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24


def mocked_user_token() -> str:
    warnings.warn("Using mocked tokens")
    return str(uuid.uuid4())


class Token(BaseModel):
    access_token: str
    user_id: str


# Hash a password using bcrypt
def get_hash(password: str) -> str:
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return str(hashed_password)


# TODO write tests for this method
def verify_hash(plain_text: str, hashed_text: str) -> bool:
    password_byte_enc = plain_text.encode("utf-8")
    hashed_byte_encoding = hashed_text.encode("utf-8")
    return bcrypt.checkpw(
        password=password_byte_enc, hashed_password=hashed_byte_encoding
    )


def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire: datetime = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # type: ignore
    return encoded_jwt


def get_current_user_id(authorization: Annotated[str | None, Header()] = None) -> str:
    if authorization is None or not authorization.strip():
        raise HTTPException(401, "Token is not set")
    try:
        payload: dict[str, Any] = jwt.decode(authorization, SECRET_KEY, algorithms=[ALGORITHM])  # type: ignore
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise HTTPException(401, "sub is not presend on JWT")
    except InvalidTokenError:
        raise HTTPException(401, "Token is not valid")
    return user_id
