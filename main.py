from User.auth import autenticar, registrar as auth_registrar
from chatbot.chatbot import trabalhar_mensagem 

def menu_inicial():
    print(""" 
    ---BANK BOT---
    1 - Fazer Login
    2 - Criar Conta
    3 - Sair""")
    return input("Escolha uma opção: ")

def cadastrar_cliente():
    print("""---Criar Conta---""")
    nome = input("Digite seu nome: ")
    cpf = input("CPF: ")
    senha = input("Senha: ")

    criar_conta = (nome, cpf, senha)
    print("Cadastro concluido", criar_conta)

def fazer_login():
    print("---Login---")
    cpf = input("CPF: ")
    senha = input("Senha: ")

    sucesso, mensagem = autenticar(cpf, senha)
    print(mensagem)

    if(sucesso):
        return cpf
    return None

def iniciar_chatbot(cpf):
    print("Chatbot: Olá! Como posso ajudar hoje?")
    print("(Digite 'sair' para encerrar)")

    while True:
        msg = input("Você: ").strip().lower() #strip para não conter espaços e lower para deixar em minusculas

        if(msg in ["sair", "exit", "quit", "tchau"]):
            print("Chatbot: Até logo!")
            break

        resposta = trabalhar_mensagem(msg, cpf)
        print("Chatbot:", resposta)



while True:
    opcao = menu_inicial()
    match(opcao):
        case "1":
            cpf = fazer_login()
            if(cpf):
                iniciar_chatbot(cpf)

        case "2":
            cadastrar_cliente()

        case "3":
            print("Encerrando sistema...")
            break

        case _:
            print("Opção inválida! Tente novamente.")