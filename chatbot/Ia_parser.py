from openai import OpenAI
import json #importaro  json
import os
from dotenv import load_dotenv #importação para o .env 

load_dotenv()

client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY")) #Utilização da API

def interprertar_mensagem(mensagem):
    #promt_sistema é para definir quem será a Ia
    prompt_sistema = f""" 
    você é um parser bancário. Interprete a frase do usuário e retorne em JSON.
    Exemplos de intenções válidas:
    - consultar_saldo
    - sacar
    - depositar
    - transferir

    A mensagem é: "{mensagem}"

    Retorne SOMENTE um JSON com as chaves: "intencao", "valor" (numérico) e "destino".
    Se não houver valor ou destino, use null ou 0.
    """
    try:
        resposta = client.chat.completions.create(
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": mensagem}
            ]
        )
    except Exception as e:
        print(f"Erro ao interpretar: {e}")
        return None

    json_str = resposta.output[0].content[0].text
    return json.loads(json_str)