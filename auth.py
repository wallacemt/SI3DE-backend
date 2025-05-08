from argon2 import PasswordHasher
import jwt
from datetime import datetime, timedelta
from bson import ObjectId
from config import JWT_SECRET
ph = PasswordHasher()

SECRET_KEY = JWT_SECRET

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    try:
        ph.verify(hashed, password)
        return True
    except:
        return False

def create_jwt(user_id: str, email: str) -> str:
    payload = {
        "sub": {"id": str(user_id), "email": email},
        "exp": datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
