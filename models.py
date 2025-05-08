from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Literal

class UserSchema(BaseModel):
    nome: str
    email: EmailStr
    password: str
    role: Literal["student", "teacher", "carreiras"]
    acessAt: datetime
