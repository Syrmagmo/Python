"""
entrada de dados

"""
nome = input("Digite seu nome?")
idade = input("Qual a sua idade?")

ano_nascimento = 2022 - int(idade)  #Devemos atribuir o inteiro para o Idade pois ele esta em formato SRT

print(f'O usuario digitou {nome} e o tipo da variavel e' 
      f'{type(nome)}.'
      f'{nome} nasceu em {ano_nascimento}.')
