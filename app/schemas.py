# Estrutura na API (entradas/saídas)

from pydantic import BaseModel, EmailStr
import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime.datetime

    class Config:
        from_attributes = True