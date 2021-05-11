def web_usuario(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF" : kwargs["CPF"] if "CPF" in kwargs else ""
    }

def nome_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""


def usuario_db(usuario):
    return {
        "id": usuario["id"],
        "nome_completo": usuario["nome_completo"],
        "CPF": usuario["CPF"]
    }

def web_diretor(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }