def web_usuario(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "cpf" : kwargs["cpf"] if "cpf" in kwargs else ""
    }

def usuario_db(*args):
    return {
        "nome_completo": args[0],
        "cpf": args[1],
    }