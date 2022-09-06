"""
Split, Join, Enumerate 
* Split - Dividir uma string
* Join - junta uma lista
* Enumerate - Enumerar elementos da lista # iteraveis
"""
string = "O Brasil é penta"
lista = string.split(' ')
lista1 = [
    [1,2],
    [3,4],
    [5,6],
]

for indice, valor in enumerate(lista):
    print(indice, valor)
    print(lista[indice])  #é o mesmo do codigo a cima
    
#---------------------------------------------
lista2 = [
    [0,'lincoln'],
    [1,"Richard"],
    [2,"Marques"],
]
print()
for indice, nome in lista2:
    print(indice, nome)
    
#---------------------------------------------

lista3 = ['Lincoln', 'Richard', 'Marques']
print()
for indice, nome in enumerate(lista3):
    print(indice, nome)
    

#----------------------------------------------[
    
print()
lista4 = [
    ["Essa", 'E um formato', 'de lista'],
    ['1','2','3'],
    ['4','5','6'],
]

print(lista4[1][2])


enumerada =  enumerate(lista4)
print(enumerada)  #Podemos converter 
print(list(enumerada))

enumerada2 = list(enumerate(lista4))
print(enumerada2[1][1][2])  # Priemor é o indice da lista mae
  # O segundo valor [1] é para obter o valor da lista
  # E o ultimo [2] é para obter o indice dois da lista de indice 1 
  
  # Enumerate enumera os elementos de uma lista %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=
 
  # Outra forma de fazer 
  
lista5 = [
    ["Edu","João",'Luiz'],
    ["Maria","Alice",'Joana'],
    ["Wukong","Darius",'Lulu'],
]

for v1, v2 in enumerate(lista5):  #caso queira enumerar ex enumerate(lista5, 53): ele vai começar do 53
    print(v1,v2)