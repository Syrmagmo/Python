"""
While em Python 
utilizado para realizar açoes enquanto
uma condição for verdadeira.
Requisitos: Entender condições e operadores
"""

#while True:  #Esse é um laço infinito 
#    nome = input("Qual o seu nome?")
#    print(f"Ola {nome}!")
#

#x = 0 
#while x < 100:
#    if x == 3:  #Para pular o numero
#        x = x + 1
#        continue  #Sempre que tiver a palavra continue, as proximas linhas do laço não serão lidas 
#        
#    print(x)
#    x = x + 1
#    
#print("Acabou!")

#x = 0 #coluna
#y = 0 #linha
#
#while x < 10:
#    
#    y = 0 #linha
#    
#    while y < 5:
#        print(f"Xvale {x} e Y vale {y}")
#        y += 1
#        
#    x += 1  # x = x + 1
#
#print("Acabou!")

while True:
    print()
    num_1 = input("Digite um numero: ")
    num_2 = input("Digite outro nùmero: ")
    operador = input("Digite um operador: ")
    sair = input("Deseja sair? [s]im ou [N]ão: ")

    
    if not num_1.isnumeric() or num_2.isnumeric():
        print("Você precisa digitar um Numero. ")
        continue
    
    if sair == 's':
        break
    
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print("Operador invalido!")
