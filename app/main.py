import sys
import os

# Adicionando o caminho da pasta do projeto para permitir importações corretas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Corrigindo as importações de acordo com a estrutura do projeto
from app.services.usuario_service import UsuarioService
from app.repositories.usuariorepository import UsuarioRepository
from app.database.session import Session


def main():
    # Criando a sessão do banco de dados
    db_session = Session()  # Renomeado para evitar conflito com o nome 'session'
    repository = UsuarioRepository(db_session)
    service = UsuarioService(repository)

    # Solicitando dados para o usuário.
    print("\nAdicionando usuário.")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    # Listar todos os usuários cadastrados.
    print("\nListando usuários cadastrados.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")


if __name__ == "__main__":
    os.system("cls || clear")  # Limpar a tela
    main()
