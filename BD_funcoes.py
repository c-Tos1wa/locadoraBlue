from mysql.connector import connect

dados_database = {"host":"localhost", "user":"root", "password":"root", "database":"bluecommerce"}


def query(sql, params=None):
    with connect(**dados_database) as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()


def execute(sql, params=None):
    with connect(**dados_database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit()
            return cursor.lastrowid

def inserir(tabela, colunas, valores):
    return execute(f"INSERT INTO {tabela} ({','.join(colunas)}) VALUES ({','.join(['%s' for valor in valores])})", valores)


def deletar(tabela, coluna, valor):
    execute(f"DELETE FROM {tabela} WHERE {coluna} = %s", (valor,))


def atualizar(tabela, chave, chave_valor, colunas, valores):
    set = [f"{coluna} = %s" for coluna in colunas]
    execute(f"UPDATE {tabela} SET {','.join(set)} WHERE {chave} = %s", valores + [chave_valor])


def selecionar(tabela, chave = 1, c_valor = 1):
    return query(f"SELECT * FROM {tabela} WHERE {chave} = %s", (c_valor,))


def mostrar(tabela, chave, valor):
    return query(f"SELECT * FROM {tabela} WHERE {chave} LIKE %s", (f"%{valor}%",))
