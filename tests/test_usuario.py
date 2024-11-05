import pytest
from app.config.database import SessionLocal, engine
from app.models.usuario_model import Base
from app.services.usuario_service import add_usuario, get_usuario, update_user, delete_user, list_users

Base.metadata.create_all(bind=engine)

@pytest.fixture
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_add_usuario(db):
    usuario = add_usuario(db, "João", "joao@example.com", "senha123")
    assert usuario.nome == "João"
    assert usuario.email == "joao@example.com"

def test_get_usuario(db):
    add_usuario(db, "João", "joao@example.com", "senha123")
    usuario = get_usuario(db, "joao@example.com")
    assert usuario is not None
    assert usuario.nome == "João"

def test_update_usuario(db):
    usuario = add_usuario(db, "João", "joao@example.com", "senha123")
    updated_usuario = update_user(db, usuario.id, "João Atualizado", "joao@example.com", "nova_senha")
    assert updated_usuario
