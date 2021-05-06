from models import get_usuarios, get_diretores

def valida_usuario(nome_completo, cpf):
    if len(cpf) != 14 and nome_completo == "":
        return False

    usuario = get_usuarios(nome_completo)
    if len(usuario) > 0:
        return False

    return True