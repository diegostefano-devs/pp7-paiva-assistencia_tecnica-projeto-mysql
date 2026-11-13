from database.conexao import conectar

def buscar_tec():
    con = conectar()
    cursor = con.cursor()
  
    sql = """SELECT t.id
                FROM tecnicos t
                LEFT JOIN ordens_servico os ON t.id = os.id_tecnico AND os.status != "FINALIZADOS"
                GROUP BY t.id
                ORDER BY COUNT(os.id) ASC
                LIMIT 1"""
    cursor.execute(sql)
    resultado = cursor.fetchone()
    if not resultado:
        raise Exception("Nenhum técnico cadastrado no banco de dados.")
    return resultado[0]

def validar_id_cliente(id_cliente):
    con = conectar()
    cursor = con.cursor()
    try:
        sql = "SELECT id FROM clientes WHERE id = %s"
        cursor.execute(sql, (id_cliente,))
        resultado = cursor.fetchone()

        if not resultado:
            raise ValueError ("Cliente não cadastrado no banco de dados.")
        return resultado 
    
    finally:
        cursor.close()
        con.close()   
      


def abrir_os(ordem, id_tecnico):
    con = conectar()
    cursor = con.cursor()
    try:
        sql = "INSERT INTO ordens_servico (id_cliente, id_tecnico, aparelho, problema) VALUES (%s, %s, %s, %s)"
        valores = (
            ordem['id_cliente'], id_tecnico,
            ordem['aparelho'], ordem['problema']
        )
        cursor.execute(sql, valores)
        con.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        con.close()

def finalizar_os(id_os, status):
    con = conectar()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE ordens_servico SET status = %s WHERE id = %s", (status, id_os))
        con.commit()
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        raise e
    finally:
        cursor.close()
        con.close()


def listar_os():
    con = conectar()
    cursor = con.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM ordens_servico ORDER BY id")
        return cursor.fetchall()
    finally:
        cursor.close()
        con.close()

def listar_os_status(status):
    con = conectar()
    cursor = con.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM ordens_servico WHERE status = %s ORDER BY id", (status, ))
        resultado = cursor.fetchall()

        if not resultado:
            raise ValueError("Sem OS's com esse status.")

        return resultado
    finally:
        cursor.close()
        con.close()

