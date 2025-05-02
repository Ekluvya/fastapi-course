import os
from dotenv import load_dotenv
import datetime
import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = os.getenv("JWT_SECRET", "default-secret-for-dev")
    token_expiry_minutes = int(os.getenv("TOKEN_EXPIRY_MINUTES", 30))

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def encode_token(self, user_id: int, username: str) -> str:
        payload = {
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=self.token_expiry_minutes),
            "iat": datetime.datetime.now(datetime.timezone.utc),
            "user_id": user_id,
            "username": username
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")
    
    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            if "user_id" not in payload or "username" not in payload:
                raise HTTPException(status_code=401, detail="Invalid token payload")
            return {"user_id": payload["user_id"], "username": payload["username"]}
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
        
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)) -> dict:
        if not auth.credentials:
            raise HTTPException(status_code=401, detail="No token provided")
        return self.decode_token(auth.credentials)