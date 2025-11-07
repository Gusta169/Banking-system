import bcrypt
from database.db_connection import conectar

def registrar(nome, cpf, senha):
    con = conectar()
    cursor = con.cursor()

    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()) #bcrypt.hashpw gera um hash criptografado de uma senha
                                                                        #bycrypt.gebsalt é uma função para gerar um "salt" aleatorio para ofuscar senhas
                                                                        #sendo tambem que a chave hash que só o bycrypt conhece para encriptar

    cursor.execute("""
        Insert Into clientes (nome, cpf, senha, saldo) VALUES (%s, %s, %s, %s)""",
        (nome, cpf, senha_hash.decode("utf-8"), 0))

    con.commit()
    con.close()
    return "Conta criada"

def autenticar(cpf, senha):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("select senha from clientes WHERE cpf = %s", (cpf,))
    resultado = cursor.fetchdone() #metodo de objeto, recupera todas as linhas restantes de um conjunto de resultado de consulta de banco de dados
    con.close()

    if(resultado == False):
        return "Conta não encontrada."

    senha_hash = resultado[0].encode("utf-8")

    if(bcrypt.checkpw(senha.encode("utf-8"), senha_hash)): #"bcrypt.checkpw é utilizada para comparar uma senha em texto simples com um hash de senha que ja foi armazenada
        return True, ("Login Realizado!")
    else:
        return False, ("Senha incorreta")