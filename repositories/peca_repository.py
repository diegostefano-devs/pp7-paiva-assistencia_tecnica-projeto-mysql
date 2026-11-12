from database.conexao import conectar

def cadastrar_peca(peca):
    con = conectar()
    cursor = con.conectar()

    try:
        sql = "INSERT INTO pecas (nome, categoria, quantidade, estado, preco)"
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


def alterar(peca_id, nome, categoria, quantidade, estado, preco):
    con = conectar()
    cursor = con.cursor()
    sql = "UPDATE pecas SET nome = %s, categoria = %s, quantidade = %s, estado = %s, preco = %s WHERE id = %s"
    try:
        valores = (nome, categoria, quantidade, estado, preco, peca_id)
        cursor.execute(sql, (valores))
        con.commit()
        return cursor.rowcount > 0
    finally:
        con.close