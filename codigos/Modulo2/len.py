from pickletools import string1
import string


usuario = input("Digite seu usuario: ")
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

# Para Deixar passar apenas numeros com 6 caracteres ou + 
#if qtd_caracteres < 6:
#    print("Você precisa digitar pelo menos 6 caracteres")
#else: 
#    print("Você foi cadastrado no sistema.")


#Contas com LEN
string1 = input("Digite alguma cosia: ")
string2 = input('Digite outra coisa: ')
print(f"A quantidade de caracteres digitado foi {len(string1) + len(string2)}")

#Erros 
#print(len(12345))
#print(len(1.2))
#print(len(True))