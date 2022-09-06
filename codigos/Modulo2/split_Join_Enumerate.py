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
    
#--------------------------------------------------------------------

palavra = ''
contagem = 0

for valor in lista1:
    qtd_vezes = lista1.count(valor)
    
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f"A palavra que apareceu mais vezes é {palavra} ({contagem}x)")

#------------------------------------

for valor in lista1:
    print(valor.strip().capitalize())  #Remove o espaço no fim e no inicio # Capitalize deixa a primeira letra maiuscula 