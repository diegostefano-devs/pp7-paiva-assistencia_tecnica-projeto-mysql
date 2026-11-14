from database.conexao import conectar
from mysql.connector import IntegrityError


def validar_cpf(cpf):
    con = conectar()
    cursor = con.cursor()
    try:
        sql = "SELECT id FROM clientes WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        resultado = cursor.fetchone()
        return resultado is not None
    finally:
        cursor.close()
        con.close()

     

def cadastrar(cliente):
    con = conectar()
    cursor = con.cursor()
    try:
        sql = "INSERT INTO clientes (cpf, nome, telefone) VALUES (%s, %s, %s)"
        valores = (
            cliente['cpf'],
            cliente['nome'],
            cliente['telefone']
        )
        cursor.execute(sql, valores)
        con.commit()
        return cursor.lastrowid

    except IntegrityError:
        con.rollback()
        raise ValueError("Este CPF já consta no sistema.")
    except Exception as erro:
        con.rollback()
        raise
    finally:
        cursor.close()
        con.close()

def excluir(cpf):
    if not validar_cpf(cpf):
        raise ValueError(f"O CPF {cpf} não consta no banco de dados.")
    
    con = conectar()
    cursor = con.cursor()
    try:
        sql = "DELETE FROM clientes WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        con.commit()
        return cursor.rowcount > 0
        
    except Exception as e:
        con.rollback()
        raise
    finally:
        cursor.close()
        con.close()
        
def alterar(nome, telefone, cpf):
    if not validar_cpf(cpf):
        raise ValueError(f"O CPF {cpf} não consta no banco de dados.")
    
    con = conectar()
    cursor = con.cursor()
    try:
        sql = "UPDATE clientes SET nome = %s, telefone = %s WHERE cpf = %s"
        cursor.execute(sql, (nome, telefone, cpf))
        con.commit()
        return cursor.rowcount > 0
    except Exception as e:
        con.rollback()
        raise
    finally:
        cursor.close()
        con.close()


def listar_clientes():
    con = conectar()
    cursor = con.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM clientes ORDER BY id")
        return cursor.fetchall()
    finally:
        cursor.close()
        con.close()

