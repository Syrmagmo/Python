"""
Listas em Python 2
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
from unicodedata import digit


l2 = [1,2,3,4,5,6,7,8,9]
l2.insert(0,'Banana')
print(l2)
del(l2[0])
print(l2)
del(l2[3:5])  #Para deletar os indices que você escolher
print(l2)
 
# MAX MIM

print(max(l2))
print(min(l2))

# RANGE

l3 = list(range(1,10))  #Devemos converter para lista
print(l3)

soma = 0
for valor in l3:
    soma += valor
    print(f'{soma}+{valor}={soma}')
print(soma)

#
l4 = ['String', True, 10, -20.5]

for elemento in l4:
    print(f"O tipo de {elemento} é {type(elemento)}")
    
