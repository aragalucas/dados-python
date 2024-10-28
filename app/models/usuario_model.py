from sqlalchemy import Colum, String, Integer
from sqlalchemy.org import declarative_base
from config.database import db

base = declarative_base

class Usuario(base):
    __tabblename__ = "usuarios"
    
    id = Colum(integer, primary_key=True, autoincrement=True)
    nome = Colum(String(150))
    email = Colum(String(150))
    senha = Colum(String(150))

    def __init___(self)