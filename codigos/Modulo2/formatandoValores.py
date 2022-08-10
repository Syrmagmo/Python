"""
Formatando valores com modificadores 
:s - Texto(String)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NUMERO) f - Quantidade de casa decimais (float) :.2f 
:(caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
nome = "Lincoln"

num1= 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f"{divisao:.2f}")

num_1 = 1
print(f"{num_1:0>10}")  #O valor tera 10 casas, valores a esquerda >

num_2 = 1150
print(f"{num_2:0<10}")  #Para valores a direita utilizar o <

num_3 = 1150
print(f"{num_3:0^10}")  #Valor no centro
print(f"{nome:#^50}")  #Valor no centro
print(len(nome))

nome = "Lincoln"
nome = nome.ljust(10,'#')  #Ljust - Justifica o nome á esquerda


print(nome)
print(nome.lower())  # tudo minusculos
print(nome.upper())  # Tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas