from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        print("=" * 50)
        print("TOKEN:", token)
        print("SECRET:", settings.SECRET_KEY)
        print("ALGORITHM:", settings.ALGORITHM)

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        print("PAYLOAD:", payload)

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

        return email

    except JWTError as e:
        print("JWT ERROR:", e)
        raise credentials_exception