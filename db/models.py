from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import List, Optional, Literal
from datetime import datetime


class UserSchema(BaseModel):
    nome: str
    email: EmailStr
    password: str
    role: Literal["student", "teacher", "carreiras"]
    acessAt: datetime


class ProfileBase(BaseModel):
    curso: str
    numeroMateriasConcluidas: int = Field(..., ge=0)
    craValue: float = Field(..., ge=0.0, le=10.0)
    interesses: List[str]
    habilidades: List[str]
    turno: str
    modalidade: str
    linkedin: Optional[HttpUrl]
    github: Optional[HttpUrl]
    portfolio: Optional[HttpUrl] = None


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    user_id: str
