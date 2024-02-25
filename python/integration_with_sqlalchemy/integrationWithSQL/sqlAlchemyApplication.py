from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    # atributos
    id = Column(Integer)
