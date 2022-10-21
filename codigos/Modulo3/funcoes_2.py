"""
Funções - (def) em Python - return - (pt2)
"""
def saudacao(msg="msg padrao", nome="Usuario"):
    nome = nome.replace('i','1')
    msg = msg.replace('O','0')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)