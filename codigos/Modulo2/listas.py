"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
booleanos = True
inteiros = 10
flutuante = -10.10
strings = 'texto'

# lista podem conter varios valores dentro de uma variavel 

#       0  1  2  3      4               5     6
lista= [1, 2, 3, 4, 'Lincoln Richard', True, 10.5]  #Se pode acessar os valores de acordo com os indices
#      -7 -6  -5 -4        -3         -2     -1

string = 'ABCDE' 
# Pincipal diferença entre o String e o lista
# Caso queira pegar o indice 4 da lista ira imprimir 'Lincoln Richard'
# Já na String ira pegar apenas a letra 'E'

print(lista[1])

# Como faz pra alterar um elemento dentro da lista ?
lista[5] = 'Qualquer outra coisa'

print(lista)

# Fatiamento 
print(lista[0:3])  #[0:3] ira exibir os indices de 0 ate o 2 
print(lista[:3])  #ira exibir os indices de 0 ate o 2 
print(lista[2:])  # Exibe a partir do indice 2 ate o fim
print(lista[-1])  # Exibe o ultimo indice
print(lista[0])  #  Exive o primeiro indice
print(lista[::2])  # Exibe todos os indices pulando de 2 em 2
print(lista[::-1])  #Exibe todos os indices pulando de 2 em 2 de traz pra frente

# append, insert, pop, del, clear, extend, +

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista3 = lista1 + lista2  #Operador de + para concatenar as listas 
#ou
lista1.extend(lista2)
lista1.extend('a')  #Tambem pode ser adicionados valores desta forma 

#Append = Para adicionar um valor no final da lista
lista2.append('b')

#insert = adiciona onde quiser na lista
lista2.insert(0, 'banana')  #Deve se especificar o indice em que deve ser inserido e o valor a ser inserido 

#Pop = para deletar o ultimo indice da lista
lista2.pop()

print(lista1)
print(lista2)

#print(lista3)