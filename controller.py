from flask import Flask, jsonify, request
from models import post_usuarios, get_usuarios, delete_usuarios, put_usuarios, mostrar_usuarios, post_diretor, get_diretor, put_diretor, mostrar_diretor, delete_diretor, post_genero, get_genero, delete_genero, put_genero, mostrar_genero, post_filme, get_filme, delete_filme, put_filme, mostrar_filme
from valida import valida_usuario, valida_diretor, valida_genero, valida_filme
from serializador import web_usuario, usuario_db, nome_web, web_diretor, diretor_db, web_genero, genero_db, nome_genero_web, web_filme, filme_db, titulo_web


app = Flask(__name__)


@app.route("/usuarios", methods=['POST'])
def login():
    usuario = web_usuario(**request.json)
    if valida_usuario(**usuario):
        id_usuario = post_usuarios(**usuario)
        user_cadastro = get_usuarios(id_usuario)
        return jsonify(usuario_db(user_cadastro))
    else:
        return jsonify({"ERRO":"Este usuario não pode ser cadastrado"})

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
        return jsonify({"ERRO":"Usuário inválido"})

@app.route("/usuarios/<int:id>", methods=['DELETE'])
def apagar_usuario(id):
    try:
        delete_usuarios(id)
        return "", 204
    except:
        return jsonify({"ERRO":"Esta ação não pode ser realizada. Usuário conectado a outros itens"})

#############################################################################################################################################

@app.route("/diretores", methods=['POST'])
def inserir_diretor():
    diretor = web_diretor(**request.json)
    if valida_diretor(**diretor):
        id_diretor = post_diretor(**diretor)
        diretor_cadastrado = get_diretor(id_diretor)
        return jsonify(diretor_db(diretor_cadastrado))
    else:
        return jsonify({"ERRO": "Diretor não cadastrado!"})

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
        return jsonify({"ERRO":"Esta alteração não pode ser feita"})

@app.route("/diretores/<int:id>", methods=['DELETE'])
def deletar_diretor(id):
    try:
        delete_diretor(id)
        return 'Diretor deletado', 204
    except:
        return jsonify({"ERRO":"Esta tabela não pode ser apagada porque há outras tabelas ligada a ela"})

#####################################################################################################################################################

@app.route("/generos", methods=['POST'])
def inserir_genero():
    genero = web_genero(**request.json)
    if valida_genero(**genero):
        id_genero = post_genero(**genero)
        genero_cadastro = get_genero(id_genero)
        return jsonify(genero_db(genero_cadastro))
    else:
        return jsonify({'ERRO':"Este genero não pode ser cadastrado"})

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
        return jsonify({"ERRO":"Este genero não pode ser alterado"})

@app.route("/generos/<int:id>", methods=['DELETE'])
def apagar_genero(id):
    try:
        delete_genero(id)
        return '', 204
    except:
        return jsonify({'ERRO':"Este genero não pode ser deletado"})

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
            return jsonify({"ERRO":"Este filme não pode ser cadastrado"})


@app.route("/filmes/<int:id>", methods=['PUT', 'DELETE'])
def modificacao(id):
    if request.method == 'PUT':
        filme = web_filme(**request.json)
        if valida_filme(**filme):
            put_filme(id, **filme)
            filme_alterado = get_filme(id)
            return jsonify(filme_db(filme_alterado))
        else:
            return jsonify({'ERRO':'Este filme não pode ser alterado'})

    elif request.method == 'DELETE':
        try:
            delete_filme(id)
            return "", 204
        except:
            return jsonify({"ERRO":"A tabela FILMES não pode ser apagada, há outras tabelas ligadas a ela"})

######################################################################################################################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)