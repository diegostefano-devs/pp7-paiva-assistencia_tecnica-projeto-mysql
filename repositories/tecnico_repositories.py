from database.conexao import conectar



def cadastrar(tecnico):
    
    con = conectar()
    cursor = con.cursor()

    try:
        sql = "INSERT INTO técnico (cpf, nome, telefone) VALUES (%s, %s, %s)"
        valores = (
            tecnico['cpf'],
            tecnico['nome'],
            tecnico['telefone']
        )
        cursor.execute(sql, valores)
        con.commit()
        return cursor.lastrowid

    finally:
        cursor.close()
        con.close()


def listar_tecnico():
    con = conectar()
    cursor = con.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM técnico ORDER BY id")
        return cursor.fetchall()

    finally:
        cursor.close()
        con.close()