import psycopg2 

def conectar(): 
    conexao = psycopg2.connect(
        host="localhost",          
        database="System Bank",     
        user="postgres",           
        password="p@ssw0rd",      
        port ='5432'
)