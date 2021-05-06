from BD_funcoes import inserir, deletar, atualizar, mostrar, selecionar

#usuarios
def post_usuarios(nome_completo, cpf):
    inserir('usuarios', ['nome_completo','CPF'], [nome_completo, cpf])

def get_usuarios(nome_completo):
    return selecionar('usuarios', 'nome_completo', nome_completo)

def delete_usuarios(id):
    deletar('usuarios', 'id', id)

def put_usuarios(id, nome_completo, cpf):
    atualizar("usuarios", "id", id, ['nome_completo','cpf'], [nome_completo,cpf])


def insert_diretores(nome):
    inserir('diretores',['nome_completo'], [nome])

def get_diretores(nome):
    return mostrar('diretores', 'nome_completo', nome)


def insert_generos(nome):
    inserir('generos',['nome'], nome)

def get_generos(nome):
    return mostrar('generos', 'nome', nome)


def insert_filmes(titulo,ano,classificacao, preco, id_diretores,id_generos):
    inserir('filmes',['titulo','ano', 'classificacao', 'preco', 'id_diretores','id_generos'],[titulo, ano, classificacao, preco, id_diretores, id_generos])

