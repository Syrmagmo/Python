"""
Condições IF, ELIF e ELSE 

"""

if False:
    print("verdadeiro")  #A prioridade de codigo do Python é dada a espaços portanto o print possue 4 espaços
    print("teste teste")
elif True:
    print("Agora e verdadeiro")
    nome = input('Qual o seu nome? ')
    
    print (f'seu nome é {nome}.')
elif False:
    print('Mais uma verdadeira')
    print(22 + 22)
else:
    print('não é verdadeiro')
    print('Ola')
    
#('A minha expressão não é verdadeira.')