import mysql.connector
from mysql.connector import Error

CONFIG = {
    "host": 'localhost',
    "port" : 3306,
    "user" : "root",
    "password" : "03141116*Die",
    "database" : "assistencia_tecnica"
}

def conectar():
    try: 
        conexao = mysql.connector.connect(**CONFIG)
        if conexao.is_connected:
            return conexao
    except Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        raise

