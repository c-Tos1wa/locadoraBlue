from models import get_genero

def valida_usuario(nome_completo, CPF):
    if len(CPF) != 14 or len(nome_completo) == 0:
        return False

    return True


def valida_diretor(nome_completo):
    if nome_completo == "" or nome_completo == int:
        return False

    return True


def valida_genero(nome):
    if nome == "" or nome == int:
        return False

    return True


def valida_filme(titulo, ano, classificacao, preco, id_diretores, id_generos):
    if titulo == "" or ano < 1800:
        return False
    elif classificacao < 0 or classificacao > 18:
        return False
    elif preco == str:
        return False
    elif id_generos == 0 or id_diretores == 0:
        return False