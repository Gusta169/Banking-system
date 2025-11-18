from User.Account import Cliente
from chatbot.Ia_parser import interprertar_mensagem

def trabalhar_mensagem (mensagem, cpf):
    dados = interprertar_mensagem(mensagem)
    conta = Cliente(cpf)

    intencao = dados["intencao"]
    valor = dados["valor"]
    destino = dados["destino"]

    if(intencao == "consultar_saldo"):
        return f"Seu saldo é R$ {conta.mostrar_saldo():.2}"
    
    if(intencao == "sacar"):
        return conta.sacar(valor)

    if(intencao == "depositar"):
        return conta.depositar(valor)

    return "Desculpe, não entendi oque deve ser feito."