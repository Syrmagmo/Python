"""
Funções - def em Python (pt1)
"""
def funcao(): # Serve para definir sua propria função 
    print("Hello World!")  # Ex quero mudar a frase dentro do print, irei mudar apenas 1 vez

funcao()  # É mais facil para editar desta maneira 
funcao()
funcao()
funcao()

# Não é interessante se repetir dentro de seu proprio codigo

def saudacao(msg="msg padrao", nome="Usuario"):
    nome = nome.replace('i','1')
    msg = msg.replace('O','0')
    print(msg, nome)
    
saudacao("Olá","Lincoln")
saudacao("Oii","Lincoln Richard")
saudacao(nome="Lincoln", msg="hi")
