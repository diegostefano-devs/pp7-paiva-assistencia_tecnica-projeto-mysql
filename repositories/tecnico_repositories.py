from database.conexao import conectar



def cadastrar(tecnico):
    
    con = conectar()
    cursor = con.cursor()

    try:
        sql = "INSERT INTO tecnicos (cpf, nome, telefone) VALUES (%s, %s, %s)"
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
        cursor.execute("SELECT * FROM tecnicos ORDER BY id")
        return cursor.fetchall()

    finally:
        cursor.close()
        con.close()

def validar_cpf(cpf):
    con = conectar()
    cursor = con.cursor()

    try:
        sql = "SELECT id FROM tecnicos WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        resultado = cursor.fetchone()
        return resultado is not None

    finally:
        cursor.close()
        con.close()


def excluir(cpf):
    con = conectar()
    cursor = con.cursor()

    try:
        sql = "DELETE FROM tecnicos WHERE cpf = %s"
        cursor.execute(sql, (cpf,))
        con.commit()
        return cursor.rowcount > 0

    finally:
        cursor.close()
        con.close()


def alterar(nome, telefone, cpf):
    con = conectar()
    cursor = con.cursor()

    try:
        sql = "UPDATE tecnicos SET nome = %s, telefone = %s WHERE cpf = %s"
        cursor.execute(sql, (nome, telefone, cpf))
        con.commit()
        return cursor.rowcount > 0

    finally:
        cursor.close()
        con.close()
        