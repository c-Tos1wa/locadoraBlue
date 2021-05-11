from BD_funcoes import inserir, deletar, atualizar, mostrar, selecionar, query

#usuarios
def post_usuarios(nome_completo, CPF):
    return inserir('usuarios', ['nome_completo','CPF'], [nome_completo, CPF])

def get_usuarios(id_usuario):
    return selecionar('usuarios', 'id', id_usuario)[0]

def mostrar_usuarios(nome_completo):
    return mostrar('usuarios', 'nome_completo', nome_completo)

def delete_usuarios(id_usuario):
    deletar('usuarios', 'id', id_usuario)

def put_usuarios(id_usuario, nome_completo, CPF):
    atualizar("usuarios", "id", id_usuario, ['nome_completo','CPF'], [nome_completo, CPF])

###################################################################################################################
#diretores
def post_diretor(nome_completo):
    return inserir('diretores', ['nome_completo'], [nome_completo])

def get_diretor(id_diretor):
    return selecionar('diretores', 'id', id_diretor)[0]

def mostrar_diretor(nome_completo):
    return mostrar('diretores', 'nome_completo', nome_completo)

def put_diretor(id_diretor, nome_completo):
    atualizar('diretores', 'id', id_diretor, ['nome_completo'], [nome_completo])

def delete_diretor(id_diretor):
    deletar('diretores','id', id_diretor)

#####################################################################################################################
#generos
def post_genero(nome):
    return inserir('generos', ['nome'], [nome])

def get_genero(id_genero):
    return selecionar('generos', 'id', id_genero)[0]

def mostrar_genero(nome):
    return mostrar('generos', 'nome', nome)

def put_genero(id_genero, nome):
    atualizar('generos', 'id', id_genero, ['nome'], [nome])

def delete_genero(id_genero):
    deletar('generos','id', id_genero)

##################################################################################################################################################
#filmes
def post_filme(titulo, ano, classificacao, preco, id_diretores,id_generos):
    return inserir('filmes', ['titulo','ano', 'classificacao', 'preco', 'id_diretores','id_generos'], [titulo, ano, classificacao, preco, id_diretores, id_generos])

def get_filme(id_filme):
    return selecionar('filmes', 'id', id_filme)[0]

def mostrar_filme(titulo):
    return mostrar('filmes','titulo', titulo)

def put_filme(id_filme, titulo, ano, classificacao, preco, id_diretores, id_generos):
    atualizar('filmes', 'id', id_filme, ['titulo', 'ano', 'classificacao', 'preco', 'id_diretores', 'id_generos'], [titulo, ano, classificacao, preco, id_diretores, id_generos])

def delete_filme(id_filme):
    deletar('filmes', 'id', id_filme)

#######################################################################################################################################################
#locações
def post_aluguel(data_inicio, data_final, id_usuarios,id_filmes):
    return inserir('locacoes', ['data_inicio', 'data_final', 'id_usuarios', 'id_filmes'], [data_inicio, data_final, id_usuarios, id_filmes])

def join_locacoes_usuarios():
    return query("SELECT locacoes.id_usuarios FROM usuarios INNER JOIN locacoes ON locacoes.id_usuarios = usuarios.id")

def join_locacoes_filmes_usuarios():
    return query("SELECT "
                 "locacoes.id_filmes as id_filme,"
                 "usuarios.nome_completo as nome_do_usuario,"
                 "filmes.titulo as titulo_do_filme,"
                 "locacoes.data_inicio as data_da_locacao,"
                 "pagamento.status as status_pgto"
                 "FROM locacoes"
                 "INNER JOIN usuarios ON locacoes.id_usuarios = usuarios.id"
                 "INNER JOIN filmes ON locacoes.id_filmes = filmes.id")

def join_locacoes_pagamento():
    return query("SELECT pagamento.id_locacoes FROM pagamento INNER JOIN pagamento ON pagamento.id_locacoes = pagamento.id")

def get_aluguel(id_locacoes):
    return selecionar('locacoes', 'id', id_locacoes)[0]

#######################################################################################################################################################
#pagamentos
def post_pagamento(tipo, status, codigo_pagamento, valor, data, id_locacoes):
    return inserir('pagamento', ['tipo', 'status','codigo_pagamento', 'valor', 'data', 'id_locacoes'],[tipo, status, codigo_pagamento, valor, data, id_locacoes])

def get_pagamento(id_pagamento):
    return selecionar('pagamento','id', id_pagamento)[0]

#######################################################################################################################################################