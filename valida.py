from models import get_usuarios, get_diretores

def valida_usuario(nome_completo, CPF):
    if len(CPF) != 14:
        return False

    if len(nome_completo) == 0:
        return False

    return True


def valida_diretor(nome_completo):
    if nome_completo == "":
        return False

    return True