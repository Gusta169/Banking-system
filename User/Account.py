from database.db_connection import conectar

class Cliente:
    def __init__(self, nome, cpf, saldo):
        self.cpf = cpf
    
    def mostrar_saldo(self):
        pass