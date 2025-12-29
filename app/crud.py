from sqlalchemy.orm import Session
from app.models import User

# Função que retorna um usuário pelo email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
    
# Função que cria um usuário no banco
def create_user_db(db: Session, e: str, pw: str):    
    
    # Criando objeto User
    new_user= User(email=e, password=str(pw))
    
    # Adicionando ao banco
    db.add(new_user)

    try:
        db.commit()
        # Caso funcione, atualizar objeto para receber os valores de ID e Created_At
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        raise e