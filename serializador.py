def web_usuario(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else ""
    }

def nome_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""

def usuario_db(usuario):
    return {
        "id": usuario["id"],
        "nome_completo": usuario["nome_completo"],
        "CPF": usuario["CPF"]
    }
####################################################################################################################
def web_diretor(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }

def diretor_db(diretor):
    return {
        "id": diretor['id'],
        'nome_completo':diretor['nome_completo']
    }
#####################################################################################################################
def web_genero(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else ""
    }

def genero_db(genero):
    return {
        "id": genero['id'],
        "nome": genero['nome']
    }

def nome_genero_web(**kwargs):
    return kwargs['nome'] if 'nome' in kwargs else ""

###################################################################################################################
def web_filme(**kwargs):
    return {
        "titulo":kwargs['titulo'] if "titulo" in kwargs else "",
        "ano":kwargs['ano'] if 'ano' in kwargs else "",
        "classificacao": kwargs['classificacao'] if "classificacao" in kwargs else "",
        "preco": kwargs['preco'] if 'preco' in kwargs else "",
        "id_diretores": kwargs['id_diretores'] if 'id_diretores' in kwargs else "",
        "id_generos": kwargs['id_generos'] if 'id_generos' in kwargs else ""
    }

def titulo_web(**kwargs):
    return kwargs ['titulo'] if 'titulo' in kwargs else ""

def filme_db(filme):
    return {
        'id': filme['id'],
        'titulo':filme['titulo'],
        'classificacao':filme['classificacao'],
        'preco':str(filme['preco']),
        'id_diretor':filme['id_diretores'],
        'id_genero':filme['id_generos']
    }