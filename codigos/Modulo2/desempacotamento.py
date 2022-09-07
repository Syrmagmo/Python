"""
desempacotamento de lista em Python
"""
lista = ["lincoln", "Richard", "joaozinho",1,2,3,4,5,6,7,8,9,100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista
print(n1,n2)

# o * serve para criar outra lista ex lincoln richard ["joazinho", 1 , 2 ,3 ,4 ,5,6 etc]
# Casp nao for utilizar o restante da lista coloque *_