import mysql.connector
from mysql.connector import Error

CONFIG = {
    "host": 'localhost',
    "port" : 3306,
    "user" : "root",
<<<<<<< HEAD
    "password" : "sua senha",
=======
    "password" : "040604",
>>>>>>> 0453d309f203cc3bcb8bec278e9dca8e04c0d6b4
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

