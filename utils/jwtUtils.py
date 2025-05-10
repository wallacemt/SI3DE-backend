import jwt
from datetime import datetime, timedelta
from config.config import JWT_SECRET


SECRET_KEY = JWT_SECRET
ALGORITHM = "HS256"

def create_jwt_token(user_id: str, email: str, role: str) -> str:
    payload = {
        "sub": str(user_id),  
        "email": email,
        "role": role,
        "exp": datetime.utcnow() + timedelta(days=1),
        "iat": datetime.utcnow()
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_jwt(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        print("Token expirado")
        raise
    except jwt.InvalidTokenError as e:
        print(f"Token inválido: {e}")
        raise

