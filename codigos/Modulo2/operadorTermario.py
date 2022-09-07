"""
Operador ternario Em Python
"""
logged_user = False  #Simulando se esta logado

if logged_user:  #Si estiver logado mensagem logado
    msg = 'Usuario logado'
else:  #Si estiver DESLOGADO usuario precisa logar
    msg = "Usiario precisa logar"
print(msg)

#------------------- Outra maneira de fazer

logged_user = True
msg = "Usiaro logado." if logged_user else "Usuario precisa logar"
#MSG - criando uma variavel qualquer com um valor definido
#Com o if verifico a condição ex ==True
# Elese Para caso a condição anterior for falça

print(msg)

#------------------------------------------
idade = 18

if idade >= 18:
    print("Pode acessar.")
else:
    print("Não pode acessar ")

print(msg)
#------------------------- Outra forma de fazer

idade = input("Qual a sua idade?")
if not idade.isnumeric():
    print('Vocêprecisa digitar apenas numeros!')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = "Pode acessar" if e_de_maior else "Não pode acessar." 
    print (msg)