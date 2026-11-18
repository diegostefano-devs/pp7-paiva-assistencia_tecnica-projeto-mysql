from database.conexao import conectar
from mysql.connector import IntegrityError

def cadastrar_peca_db(peca):
    con = conectar()
    cursor = con.cursor()

    try:
        sql = "INSERT INTO pecas (nome, categoria, quantidade, estado, preco) VALUES (%s, %s, %s, %s, %s)"
        valores = (
            peca['nome'],
            peca['categoria'],
            peca['quantidade'],
            peca['estado'],
            peca['preco']
        )

        cursor.execute(sql, valores)
        con.commit()
        return cursor.lastrowid
    except Exception as e:
        raise        
    finally:
        cursor.close()
        con.close()


def excluir_peca(peca_id):
    con = conectar()
    cursor = con.cursor()

    try:
        sql = "DELETE FROM pecas WHERE id = %s"
        cursor.execute(sql, (peca_id,))
        con.commit()
        return cursor.rowcount > 0
    except IntegrityError:
        con.rollback()
        raise ValueError("Esta peça não pode ser excluída porque está vinculada a Ordens de Serviço.")
    
    except Exception as e:
        con.rollback()
        raise
    finally:
        cursor.close()
        con.close()



def buscar_peca(id_peca):
    con = conectar()
    cursor = con.cursor(dictionary=True)
    try:
        cursor.execute("SELECT nome, preco FROM pecas WHERE id = %s", (id_peca, ))
        return cursor.fetchone()
    finally:
        cursor.close()
        con.close()

def listar_peca():
    con = conectar()
    cursor = con.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM pecas ORDER BY id")
        return cursor.fetchall()
    finally:
        cursor.close()
        con.close()


def alterar_peca(peca_id, nome, categoria, quantidade, estado, preco):
    con = conectar()
    cursor = con.cursor()
    sql = "UPDATE pecas SET nome = %s, categoria = %s, quantidade = %s, estado = %s, preco = %s WHERE id = %s"
    try:
        valores = (nome, categoria, quantidade, estado, preco, peca_id)
        cursor.execute(sql, (valores))
        con.commit()
        return True
    except Exception as e:
        raise
    finally:
        cursor.close()
        con.close