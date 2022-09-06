"""
Split, Join, Enumerate 
* Split - Dividir uma string
* Join - junta uma lista
* Enumerate - Enumerar elementos da lista # iteraveis
"""

string = "Brasil exa, Campeão"
lista1 = string.split(' ')  #Divide pelos espaços
lista1 = string.split(',')  #Divide pelas virgulas

print(lista1)

for valor in lista1:
    print(F'A palavra {valor} apareceu {lista1.count(valor)} vez')