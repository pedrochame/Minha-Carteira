from fastapi import APIRouter, Depends, HTTPException
from app.schemas import UserCreate, UserResponse
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from sqlalchemy.orm import Session
from argon2 import PasswordHasher
from app import crud

router_users = APIRouter()

# Rota de criação de usuário
@router_users.post("/users",status_code=201, response_model=UserResponse)
def create_user(user:UserCreate, db:Session = Depends(get_db)):
    
    # Antes de tudo, verificar se já existe um usuário com o email informado
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Erro: Email já cadastrado.")

    # Hash da senha recebida
    password_hash = PasswordHasher().hash(user.password)

    # Chamada à função CRUD que irá registrar o usuário no banco e retornar um objeto UserResponse
    try:
        return crud.create_user_db(db, user.email, password_hash)
    except IntegrityError as ie:
        # Caso dê errado, disparar exceção que indica erro de integridade
        raise HTTPException(status_code=409, detail = "Erro: Dados duplicados.")
    except Exception as e:
        # Caso dê errado, disparar exceção generalista
        raise HTTPException(status_code=500, detail = "Erro: "+str(e))