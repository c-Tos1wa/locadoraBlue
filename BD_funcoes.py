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
    execute(f"insert into {tabela} ({','.join(colunas)}) values ({','.join(['%s' for valor in valores])})", valores)


def deletar(tabela, coluna, valor):
    execute(f"delete from {tabela} where {coluna} = %s", (valor,))


def atualizar(tabela, chave, chave_valor, colunas, valores):
    set = [f"{coluna} = %s" for coluna in colunas]
    execute(f"update {tabela} set {','.join(set)} where {chave} = %s", valores + [chave_valor])


def selecionar(tabela, chave = 1, c_valor = 1):
    return query(f"select * from {tabela} where {chave} = %s",(c_valor,))


def mostrar(tabela, chave, valor):
    return query(f"select * from {tabela} where {chave} like %s", (f"%{valor}%",))
