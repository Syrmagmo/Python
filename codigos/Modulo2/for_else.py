
variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):  #Startswith = Metodo de verificação
        #Lower() = serve para transofrmar a string toda em minuscula
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)