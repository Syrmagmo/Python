usuario = input("Nome de usuario: ")
senha = input("senha do usuario: ")

usuario_bd = "Lincoln"
senha_bd = "123456"

if usuario_bd == usuario and senha_bd == senha:
    print("Você esta logado no sistema")
else:
    print("Usuario ou senha invalido")