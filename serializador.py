import uuid
import random
import datetime

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

########################################################################################################################
def web_aluguel(**kwargs):
    return {
        "data_inicio":kwargs['data_inicio'] if "data_inicio" in kwargs else "",
        "data_final":kwargs['data_final'] if "data_final" in kwargs else "",
        "id_usuarios":kwargs['id_usuarios'] if 'id_usuarios' in kwargs else "",
        "id_filmes":kwargs['id_filmes'] if 'id_filmes' in kwargs else ""
    }

def aluguel_db(locacao):
    return{
        'id':locacao['id'],
        'data_inicio':datetime.strftime('%d-%m-%Y %H:%M:%S'(locacao['data_inicio'])),
        'data_final':datetime.strftime('%d-%m-%Y %H:%M:%S'(locacao['data_final'])),
        'id_usuarios':locacao['id_usuarios'],
        'id_filmes':locacao['id_filmes']
    }

########################################################################################################################
def web_pagamento(**kwargs):
    return {
        'tipo':kwargs['tipo'] if 'tipo' in kwargs else "",
        'status':kwargs['status'] if 'status' in kwargs else "",
        'codigo_pagamento':kwargs['codigo_pagamento'] if 'codigo_pagamento' in kwargs else "",
        'valor':kwargs['valor'] if 'valor' in kwargs else "",
        'data':kwargs['data'] if 'data' in kwargs else "",
        "id_locacoes":kwargs['id_locacoes'] if 'id_locacoes' in kwargs else ""
    }

def pagamento_db(args):
    return{
        'id':args['id'],
        'tipo':args['tipo'],
        'status':random.choice(args['status']),
        'codigo_pagamento':uuid.uuid4(args['codigo_pagamento']),
        'valor':str(args['valor']),
        'data':datetime.strftime('%d-%m-%Y %H:%M:%S'(args['data'])),
        'id_locacoes':args['id_locacoes']
    }