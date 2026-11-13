from database.conexao import conectar

def add_itens_ordens(itens_ordens, valor_fixo):
    con = conectar()
    cursor = con.cursor()
    try:
        sql = "INSERT INTO itens_ordem (id_os, id_peca, quantidade, preco_uni) VALUES (%s, %s, %s, %s)"
        valores = (
            itens_ordens['id_os'], itens_ordens['id_peca'],
            itens_ordens['quantidade'], itens_ordens['preco_uni']
        )
        cursor.execute(sql, valores)

        sql_soma = "SELECT SUM(quantidade * preco_uni) FROM itens_ordem WHERE id_os = %s"
        cursor.execute(sql_soma, (itens_ordens['id_os'],))
        resultado_soma = cursor.fetchone()[0]
        total_pecas = resultado_soma if resultado_soma is not None else 0

        sql_ordem = "UPDATE ordens_servico SET status = 'AGUARDANDO APROVACAO', valor_fixo = %s, valor_total = %s WHERE id = %s" 
        cursor.execute(sql_ordem, (valor_fixo, total_pecas, itens_ordens['id_os']))
        con.commit()
    except Exception as e:
        con.rollback()
        raise e
    finally:
        cursor.close()
        con.close()

def validar_os(id_os):
    con = conectar()
    cursor = con.cursor(dictionary=True)
    try:
        sql = "SELECT id FROM ordens_servico WHERE id = %s"
        cursor.execute(sql, (id_os,))
        resultado =  cursor.fetchone()

        if not resultado:
            raise ValueError("OS não encontrada no banco de dados.")

        return resultado['id']
    finally:
        cursor.close()
        con.close()

def validar_peca(id_peca):
    con = conectar()
    cursor = con.cursor(dictionary=True)
    try:
        sql = "SELECT id FROM pecas WHERE id = %s"
        cursor.execute(sql, (id_peca,))
        resultado =  cursor.fetchone()

        if not resultado:
            raise ValueError("Peça não encontrada no banco de dados.")

        return resultado['id']
    finally:
        cursor.close()
        con.close()