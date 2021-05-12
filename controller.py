from flask import Flask, jsonify, request
from models import post_usuarios, get_usuarios, delete_usuarios, put_usuarios, mostrar_usuarios, post_diretor, get_diretor, put_diretor, mostrar_diretor, delete_diretor, post_genero, get_genero, delete_genero, put_genero, mostrar_genero
from models import post_filme, get_filme, delete_filme, put_filme, mostrar_filme, post_aluguel, get_aluguel, put_aluguel, delete_aluguel, mostrar_aluguel, post_pagamento, get_pagamento, put_pagamento, delete_pagamento, mostrar_pagamento
from valida import valida_usuario, valida_diretor, valida_genero, valida_filme, valida_pagamento, valida_aluguel
from serializador import web_usuario, usuario_db, nome_web, web_diretor, diretor_db, web_genero, genero_db, nome_genero_web, web_filme, filme_db, titulo_web, web_aluguel, aluguel_db, web_pagamento, pagamento_db
from datetime import datetime, timedelta
import random

app = Flask(__name__)


@app.route("/usuarios", methods=['POST'])
def login():
    usuario = web_usuario(**request.json)
    if valida_usuario(**usuario):
        id_usuario = post_usuarios(**usuario)
        user_cadastro = get_usuarios(id_usuario)
        return jsonify(usuario_db(user_cadastro))
    else:
        return jsonify({"erro":"Este usuario não pode ser cadastrado"})

@app.route("/usuarios", methods=['GET'])
def checar_usuario():
    nome_usuario = nome_web(**request.args)
    usuarios = mostrar_usuarios(nome_usuario)
    dado_usuario = [usuario_db(usuario) for usuario in usuarios]
    return jsonify(dado_usuario)

@app.route("/usuarios/<int:id>", methods=['PUT', 'PATCH'])
def alterar_cadastro(id):
    usuario = web_usuario(**request.json)
    if valida_usuario(**usuario):
        put_usuarios(id, **usuario)
        usuario_alterado = get_usuarios(id)
        return jsonify(usuario_db(usuario_alterado))
    else:
        return jsonify({"erro":"Usuário inválido"})

@app.route("/usuarios/<int:id>", methods=['DELETE'])
def apagar_usuario(id):
    try:
        delete_usuarios(id)
        return "", 204
    except:
        return jsonify({"erro":"Esta ação não pode ser realizada. Usuário conectado a outros itens"})

#############################################################################################################################################

@app.route("/diretores", methods=['POST'])
def inserir_diretor():
    diretor = web_diretor(**request.json)
    if valida_diretor(**diretor):
        id_diretor = post_diretor(**diretor)
        diretor_cadastrado = get_diretor(id_diretor)
        return jsonify(diretor_db(diretor_cadastrado))
    else:
        return jsonify({"erro": "Diretor não cadastrado!"})

@app.route("/diretores", methods=['GET'])
def buscar_diretor():
    nome_diretor = nome_web(**request.args)
    diretores = mostrar_diretor(nome_diretor)
    dado_diretor = [diretor_db(diretor) for diretor in diretores]
    return jsonify(dado_diretor)

@app.route("/diretores/<int:id>", methods=['PUT'])
def alterar_diretor(id):
    diretor = web_diretor(**request.json)
    if valida_diretor(**diretor):
        put_diretor(id, **diretor)
        diretor_alterado = get_diretor(id)
        return jsonify(diretor_db(diretor_alterado))
    else:
        return jsonify({"erro":"Esta alteração não pode ser feita"})

@app.route("/diretores/<int:id>", methods=['DELETE'])
def deletar_diretor(id):
    try:
        delete_diretor(id)
        return 'Diretor deletado', 204
    except:
        return jsonify({"erro":"Esta tabela não pode ser apagada porque há outras tabelas ligada a ela"})

#####################################################################################################################################################

@app.route("/generos", methods=['POST'])
def inserir_genero():
    genero = web_genero(**request.json)
    if valida_genero(**genero):
        id_genero = post_genero(**genero)
        genero_cadastro = get_genero(id_genero)
        return jsonify(genero_db(genero_cadastro))
    else:
        return jsonify({'erro':"Este genero não pode ser cadastrado"})

@app.route("/generos", methods=['GET'])
def buscar_genero():
    nome_genero = nome_genero_web(**request.args)
    generos = mostrar_genero(nome_genero)
    dado_genero = [genero_db(genero) for genero in generos]
    return jsonify(dado_genero)

@app.route("/generos/<int:id>", methods=['PUT'])
def alterar_genero(id):
    genero = web_genero(**request.json)
    if valida_genero(**genero):
        put_genero(id, **genero)
        genero_alterado = get_genero(id)
        return jsonify(genero_db(genero_alterado))
    else:
        return jsonify({"erro":"Este genero não pode ser alterado"})

@app.route("/generos/<int:id>", methods=['DELETE'])
def apagar_genero(id):
    try:
        delete_genero(id)
        return '', 204
    except:
        return jsonify({'erro':"Este genero não pode ser deletado"})

######################################################################################################################################################

@app.route("/filmes", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        nome_filme = titulo_web(**request.args)
        filmes = mostrar_filme(nome_filme)
        dado_filme = [filme_db(filme) for filme in filmes]
        return jsonify(dado_filme)

    elif request.method == 'POST':
        filme = web_filme(**request.json)
        if valida_filme(**filme):
            id_filme = post_filme(**filme)
            filme_cadastro = get_filme(id_filme)
            return jsonify(filme_db(filme_cadastro))
        else:
            return jsonify({"erro":"Este filme não pode ser cadastrado"})


@app.route("/filmes/<int:id>", methods=['PUT', 'DELETE'])
def modificacao(id):
    if request.method == 'PUT':
        filme = web_filme(**request.json)
        if valida_filme(**filme):
            put_filme(id, **filme)
            filme_alterado = get_filme(id)
            return jsonify(filme_db(filme_alterado))
        else:
            return jsonify({'erro':'Este filme não pode ser alterado'})

    elif request.method == 'DELETE':
        try:
            delete_filme(id)
            return "", 204
        except:
            return jsonify({"erro":"A tabela FILMES não pode ser apagada, há outras tabelas ligadas a ela"})

######################################################################################################################################################

@app.route("/locacoes", methods=['POST', 'GET'])
def cadastro_locacao():
    if request.method == 'POST':
        aluguel = web_aluguel(**request.json)
        hoje = datetime.now()
        data_devolucao = hoje + timedelta(hours=48)
        if valida_aluguel(**aluguel):
            id_aluguel = post_aluguel(hoje, data_devolucao, **aluguel)
            aluguel_cadastro = get_aluguel(id_aluguel)
            return jsonify(aluguel_db(aluguel_cadastro))
        else:
            return jsonify({"erro":"não foi possível efetuar a locação"})

    elif request.method == 'GET':
        aluguel = web_aluguel(**request.args)
        locacoes = mostrar_aluguel(aluguel)
        dado_locacao = [aluguel_db(locacao) for locacao in locacoes]
        return jsonify(dado_locacao)

@app.route("/locacoes/<int:id>", methods=['PUT', 'DELETE'])
def alterar_locacao(id):
    if request.method == 'PUT':
        aluguel = web_aluguel(**request.json)
        if valida_aluguel(**aluguel):
            put_aluguel(id, **aluguel)
            locacao_alterada = get_aluguel(id)
            return jsonify(aluguel_db(locacao_alterada))
        else:
            return jsonify({"erro":"não é possível alterar a locação"})

    elif request.method == 'DELETE':
        try:
            delete_aluguel(id)
            return "", 204
        except:
            return jsonify({"erro":"não é possivel apagar esta locação"})

###########################################################################################################################################

@app.route("/pagamentos", methods=['POST'])
def cadastro_pagamento():
    pago = web_pagamento(**request.json)
    pgto = ('aprovado', 'reprovado', 'em análise')
    status_pgto = random.choice(pgto)
    data_pgto = datetime.now()
    codigo = str(random.randint(0, 1000))
    if valida_pagamento(**pago):
        id_pago = post_pagamento(status_pgto, codigo, data_pgto, **pago)
        pgto_cadastro = get_pagamento(id_pago)
        return jsonify(pagamento_db(pgto_cadastro))
    else:
        return jsonify({"erro":"pagamento não efetuado"})

@app.route("/pagamentos", methods=['GET'])
def mostrar_pagamento():
    pgto = web_pagamento(**request.args)
    pagamentos = mostrar_pagamento(pgto)
    dado_pagamento = [pagamento_db(pagamento) for pagamento in pagamentos]
    return jsonify(dado_pagamento)

@app.route("/pagamentos/<int:id>", methods=['PUT'])
def alterar_pgto(id):
    pagamento = web_pagamento(**request.json)
    if valida_pagamento(**pagamento):
        put_pagamento(id, **pagamento)
        pagamento_alterado = get_pagamento(id)
        return jsonify(pagamento_db(pagamento_alterado))
    else:
        return jsonify({"erro":"esta alteração não pode ser feita"})

@app.route("/pagamentos/<int:id>", methods=['DELETE'])
def deletar_pagamento(id):
    try:
        delete_pagamento(id)
        return "", 204
    except:
        return jsonify({"erro":"esta ação não pode ser realizada"})

#######################################################################################################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)