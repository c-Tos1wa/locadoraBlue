from flask import Flask, jsonify, request
from BD_funcoes import mostrar, selecionar
from models import post_usuarios, get_usuarios, delete_usuarios, put_usuarios
from valida import valida_usuario
from serializador import web_usuario, usuario_db

app = Flask(__name__)


@app.route("/usuarios", methods=['POST'])
def login():
    usuario = web_usuario(**request.json)
    if valida_usuario(**usuario):
        post_usuarios(**usuario)
        user = get_usuarios(usuario['nome_completo'])
        return jsonify(usuario_db(user))
    else:
        return jsonify({"erro":"Usuário Inválido"})



#@app.route("/usuarios/<int:id>", methods=['PUT'])
#def logon(id):
#    usuario = web_usuario(**request.json)
#    if valida_usuario(**usuario):
#        put_usuarios(**usuario)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)