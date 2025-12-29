from fastapi import FastAPI
from app.routes.users import router_users
from app.database import Base,engine
from app import models

# Criação das tabelas, a partir dos modelos
Base.metadata.create_all(bind=engine)

# Criação da aplicação
app = FastAPI()

# Incluindo rotas na aplicação
app.include_router(router_users)