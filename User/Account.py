from database.db_connection import conectar

class Cliente:
    def __init__(self, cpf):
        self.cpf = cpf #inicialização da Classe

    def mostrar_saldo(self):
        con = conectar() #conexão com o banco de dados
        cursor = con.cursor() 
        cursor.execute("SELECT saldo FROM clientes WHERE cpf = %s", (self.cpf,)) #Localização do cliente utilizando o cpf para saber o saldo
        saldo = cursor.fetchone() #Colocando o saldo do banco de dados em uma variavel
        con.close() #Fechando a conexão com o banco de dados
        return saldo[0] #Retornar o saldo para a função
    
    def depositar(self, valor_a_depositar):
        if(valor_a_depositar <= 0):
            return "O valor do depósito deve ser positivo."
            
        saldo_atual = self.mostrar_saldo()
        
        if(saldo_atual == None):
            return "Conta não encontrada."

        novo_saldo = saldo_atual + valor_a_depositar
        
        con = conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE clientes SET saldo = %s WHERE cpf = %s", (novo_saldo, self.cpf)) #Atualiza o saldo do cliente no banco
        con.commit()
        con.close()
        
        return f"Depósito de R$ {valor_a_depositar:.2f} realizado. Novo saldo: R$ {novo_saldo:.2f}"
    
    def sacar(self, valor_a_sacar):
        saldo = self.mostrar_saldo() #utiliza da função mostrar_saldo feita antes para saber o saldo atual
        if(saldo == None):
            return "Conta não encontrada"
        
        if(valor_a_sacar > saldo):
            return "Saldo insuficiente"
        
        novo_saldo = saldo - valor_a_sacar
        con = conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE clientes SET saldo =%s WHERE cpf = %s", (novo_saldo, self.cpf))
        con.commit()
        con.close()
        return f"Saque de {valor_a_sacar:.2f} realizado. Saldo atual: R$ {novo_saldo:.2f}"
