from BD_funcoes import inserir, deletar, atualizar, mostrar, selecionar

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
    return inserir('generos', ['nome'], nome)

def get_genero(id_genero):
    return selecionar('generos', 'id', id_genero)[0]

def mostrar_genero(nome):
    return mostrar('generos', 'nome', nome)

def put_genero(id_genero, nome):
    atualizar('genero', 'id', id_genero, ['nome'], [nome])

def delete_genero(id_genero):
    deletar('generos','id', id_genero)

##################################################################################################################################################

#filmes
def post_filme(titulo, ano, classificacao, preco, id_diretores,id_generos):
    return inserir('filmes', ['titulo','ano', 'classificacao', 'preco', 'id_diretores','id_generos'], [titulo, ano, classificacao, preco, id_diretores, id_generos])

def get_filme(id_filme):
    return selecionar('filmes', id_filme)[0]

def mostrar_filme(titulo):
    return mostrar('filmes','titulo', titulo)

def put_filme(id_filme, titulo, ano, classificacao, preco, id_diretor, id_genero):
    atualizar('filmes', 'id', id_filme, ['titulo', 'ano', 'classificacao', 'preco', 'id_diretores', 'id_generos'],[titulo, ano, classificacao, preco, id_diretor, id_genero])

def delete_filme(id_filme):
    deletar('filmes', 'id', id_filme)