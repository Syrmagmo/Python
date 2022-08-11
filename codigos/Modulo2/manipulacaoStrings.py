"""
Manipulando strings 
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funçoes built-in len, abs, type, print, etc...
Essa funçoes podem ser usadas diretamente em cada tipo

"""
# positivos  [012345678]
texto      = "Python s2"
# negativos -[987654321]

nova_string = texto [-9:-3]  #para exibir os caracteres escolhidos 
print(nova_string)

nova_string = texto [0:-1]  #Para excluir um caracter
print(nova_string)

nova_string = texto [0:6:2]  #O numero 2 representa quantas casas devem ser puladas
print(nova_string)
