from app.sqlalchemy.orm import Session
from app.UsuarioRepository import create_usuario, get_usuario_by_email, update_usuario, delete_usuario, get_usuarios
def add_usuario(db: Session, nome: str, email: str, senha: str):
    if len(senha) < 6:
        raise ValueError("A senha precisa ter pelo menos 6 caracteres.")
    if not email or "@" not in email:
        raise ValueError("Email inválido.")
    if get_usuario_by_email(db, email):
        raise ValueError("Já existe um usuário com esse e-mail.")
    return create_usuario(db, nome, email, senha)

def get_usuario(db: Session, email: str):
    return get_usuario_by_email(db, email)

def update_user(db: Session, usuario_id: int, nome: str, email: str, senha: str):
    return update_usuario(db, usuario_id, nome, email, senha)

def delete_user(db: Session, usuario_id: int):
    return delete_usuario(db, usuario_id)

def list_users(db: Session):
    return get_usuarios(db)
