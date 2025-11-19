# 🏦 Sistema Bancário Inteligente com Chatbot, IA e Segurança

Bem-vindo ao BankBot, um sistema bancário desenvolvido em Python, utilizando:

PostgreSQL como banco de dados local

Python como backend

bcrypt para criptografia de senhas

OpenAI API para interpretação de linguagem natural

Chatbot inteligente capaz de entender comandos como “quero sacar 50 reais”, “meu saldo”, “transferir 100 para João” etc.

Este projeto foi criado com foco em aprendizado, organização de código e integração com IA moderna.

## 🚀 **Tecnologias Utilizadas**

| Tecnologia     | Função                                  |
| -------------- | --------------------------------------- |
| **Python 3**   | Backend principal                       |
| **PostgreSQL** | Banco de dados local                    |
| **psycopg2**   | Driver de conexão PostgreSQL            |
| **bcrypt**     | Criptografia de senha (hash seguro)     |
| **OpenAI API** | Interpretação inteligente de intenções  |
| **dotenv**     | Leitura de variáveis de ambiente (.env) |
---
### 🎯 **Funcionalidades**

Autenticação segura
- Criação de conta com senha criptografada usando bcrypt
 
- Login seguro comparando hash da senha

**Chatbot inteligente**
- “quero sacar 50”

- “me fala meu saldo”

- “transferir 100 para o joão”

- “depositar 200 reais”

**Operações bancárias**
- Consultar saldo

- Sacar

- Depositar

- Transferir para outro usuário

- Validação de saldo e erros

**Arquitetura organizada**
```text
Banking-System/
│
├── chatbot/
│   ├── chatbot.py
│   └── Ia_parser.py
│
├── database/
│   ├── Account.py
│   ├── auth.py
│   └── ...
│
├── User/
│   ├── bot.py
│   └── ia_parser.py
│
└── main.py

### **Arquivos Principais**
```
---
🔸 auth.py

- Cria contas com hash seguro

- Autentica usuário via bcrypt

🔸 conta.py

- Contém todas as operações bancárias (saldo, saque, depósito, transferência)

🔸 ia_parser.py

- Envia a mensagem do usuário para a IA da OpenAI

- Retorna intenções em formato JSON

🔸 bot.py
- Recebe intenções da IA

- Chama métodos do modelo bancário

🔸 main.py
- Tela de login e criação de contas

- Execução principal do chatbot
---
### **🛠️ Como rodar o projeto**

1️⃣ **Instale as dependências**
pip install psycopg2 bcrypt python-dotenv openai

2️⃣ **Crie o banco de dados no PostgreSQL**
CREATE DATABASE banco_local;

3️⃣ **Configure o arquivo .env**
OPENAI_API_KEY=sua_chave_aqui

4️⃣ **Rode o sistema**
python main.py

## **Exemplos de comandos para o chatbot**
| Comando                  | Ação           |
| ------------------------ | -------------- |
| “Tenho quanto?”          | Consulta saldo |
| “Quero sacar 50 reais”   | Saque          |
| “Depositar 120”          | Depósito       |
| “Transfere 200 pro João” | Transferência  |
| “sair”                   | Encerra        |

## **Segurança**
O sistema utiliza:

- bcrypt.hashpw() para gerar hashes seguros

- bcrypt.checkpw() para validar a senha

- Armazenamento de hashes no banco (nunca a senha real)

- Evita SQL injection usando parâmetros %s

## **🤖 Inteligência Artificial**

Utiliza a ** API da OpenAI** para:

- Interpretar a intenção do usuário

- Extrair valores

- Identificar ações bancárias

###### Isso torna o sistema:

- flexível

- natural

- muito mais inteligente

#### **Projeto acadêmico e pessoal focado em melhorar conhecimento em:**

- Python

- Bancos de dados

- Segurança de sistemas

- IA aplicada

- Organização profissional de projetos
