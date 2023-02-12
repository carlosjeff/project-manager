import jwt
from datetime import datetime, timedelta
from config import Config
from utils.exceptions.http_exceptions import Unauthorized

class TokenJwt:

    algorithm = "HS256"
    time_minutes = 30

    @classmethod
    def encoder(cls, data: dict, exp: int = time_minutes):
        payload = data.copy()
        secret_key = Config.SECREY_KEY

        expires = datetime.utcnow() + timedelta(minutes=exp)
        payload.update({"exp": expires})

        token = jwt.encode(payload=payload, key=secret_key, algorithm=cls.algorithm)

        return token

    @classmethod
    def verify(cls, token: str):
        secret = Config.SECREY_KEY
        try:
            token = token.replace("Bearer ", "")
            data = jwt.decode(token, secret, algorithms=[cls.algorithm])
            return data.get("sub")
        except jwt.DecodeError:
            raise Unauthorized("Invalid token")
        except jwt.ExpiredSignatureError:
            raise Unauthorized("Token expired")