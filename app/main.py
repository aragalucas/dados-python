from sqlalchemy.orm import Session
from app.config.database import SessionLocal, engine
from app.models.usuario_model import Base
from app.services.usuario_service import add_usuario, get_usuario, update_user, delete_user, list_users

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def menu():
    while True:
        print("\nSENAI SOLUTION")
        print("1 - Adicionar usuário")
        print("2 - Pesquisar um usuário")
        print("3 - Atualizar dados de um usuário")
        print("4 - Excluir um usuário")
        print("5 - Exibir todos os usuários cadastrados")
        print("0 - Sair")
        
        opcao = input("Informe a opção desejada: ")
        
        with next(get_db())) as db:
            if opcao == "1":
                nome = input("Informe o nome do usuário: ")
                email = input("Informe o e-mail do usuário: ")
                senha = input("Informe a senha do usuário: ")
                try:
                    usuario = add_usuario(db, nome, email, senha)
                    print(f"Usuário {usuario.nome} criado com sucesso!")
                except ValueError as e:
                    print(f"Erro: {e}")
            elif opcao == "2":
                email = input("Informe o e-mail do usuário a pesquisar: ")
                usuario = get_usuario(db, email)
                if usuario:
                    print(f"Usuário encontrado: {usuario.nome}, {usuario.email}")
                else:
                    print("Usuário não encontrado.")
            elif opcao == "3":
                usuario_id = int(input("Informe o ID do usuário a atualizar: "))
                nome = input("Informe o novo nome: ")
                email = input("Informe o novo e-mail: ")
                senha = input("Informe a nova senha: ")
                usuario = update_user(db, usuario_id, nome, email, senha)
                if usuario:
                    print(f"Usuário {usuario.nome} atualizado com sucesso!")
                else:
                    print("Usuário não encontrado.")
            elif opcao == "4":
                usuario_id = int(input("Informe o ID do usuário a excluir: "))
                usuario = delete_user(db, usuario_id)
                if usuario:
                    print(f"Usuário {usuario.nome} excluído com sucesso!")
                else:
                    print("Usuário não encontrado.")
            elif opcao == "5":
                usuarios = list_users(db)
                if usuarios:
                    for usuario in usuarios:
                        print(f"{usuario.id} - {usuario.nome} ({usuario.email})")
                else:
                    print("Nenhum usuário cadastrado.")
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    menu()
