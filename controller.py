from flask import Flask, jsonify, request
from models import post_usuarios, get_usuarios, delete_usuarios, put_usuarios, mostrar_usuarios
from valida import valida_usuario
from serializador import web_usuario, usuario_db, nome_web

app = Flask(__name__)


@app.route("/usuarios", methods=['POST'])
def login():
    usuario = web_usuario(**request.json)
    if valida_usuario(**usuario):
        id_usuario = post_usuarios(**usuario)
        user = get_usuarios(id_usuario)
        return jsonify(usuario_db(user))
    else:
        return jsonify({"erro":"Este usuario não pode ser cadastrado"})

@app.route("/usuarios", methods=['GET'])
def checar_usuario():
    nomeUsuario = nome_web(**request.args)
    usuarios = mostrar_usuarios(nomeUsuario)
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
        return jsonify({"Erro":"Este usuario não pode ser alterado"})

@app.route("/usuarios/<int:id>", methods=['DELETE'])
def apagar_usuario(id):
    try:
        delete_usuarios(id)
        return "", 204
    except:
        return jsonify({"erro":"Esta ação não pode ser realizada. Usuário conectado a outras tabelas"})


#@app.route("/diretores", methods=['POST'])





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)