import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services import usuario_service
from app.repositories import usuariorepository
from app.database import session



def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Solicitando dados para o usuário.
    print("\nAdicionando usuário.")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    # Listar todos os usuário cadastrados.
    print("\nListando usuários cadastrados.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")


if __name__ == "__main__":
    os.system("cls || clear")
    main()