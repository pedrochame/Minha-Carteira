import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Carregando valores do arquivo de configuração (.env)
load_dotenv()

# Engine → "motor" da conexão com o banco
engine = create_engine(f"{os.getenv('DB_TYPE')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

# SessionLocal → fábrica de sessões (cada sessão é uma conexão ativa)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base → classe base para declarar os modelos (tabelas)
Base = declarative_base()

def get_db():
    # Criação de uma nova sessão (conexão com o banco)
    db = SessionLocal()
    try:
        # Retorno da sessão para quem chamou (rota, função)
        yield db
    finally:
        # Quando a rota termina, volta aqui e fecha a sessão
        db.close()