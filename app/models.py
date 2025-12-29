# Estrutura no banco de dados

from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)