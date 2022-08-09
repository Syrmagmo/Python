"""
Faça um programa que peça ao usuario para digitar um numero inteiro, informe se este 
numero é par ou impar. Caso o usuario nao digite um numero inteiro, 
informe que não é um numero inteiro.
"""

"""
faça um programa que pergunte a hora ao usuario e, baseando-se no hoarario descrito, exiba a saudação apropriada. ex.
Bom dia 0-11, boa tarde 12-17 e boa noite 18-23.
"""

"""
faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva 
"Seu nome é curto"; se tiver 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva
"Seu nome é muito grande".
"""

# Exercico 1
#num1 = input("Digite um numero inteiro: ")

#if num1.isdigit():
#    num1 = int(num1)
#    
#    if num1 % 2 == 0:
#        print(f"O {num1} e par")
#   else:
#        print(f"O {num1} e impar")
#else:
#    print("Isso não é um numero inteiro")

    
    
# exercicio 2 
#horario = input("Digite o horario (0-23): ")

#if horario.isdigit():
#    horario = int(horario)
#    
#    if horario < 0 or horario > 23:
#        print("O horario deve estar entre 0 e 23!")
#    elif horario <= 11:
#        print("Bom dia!")
#    elif horario <= 17:
#        print('Boa tarde')
#    else:
#        print('Boa noite!')
#    else:
#        print("Digite um horario de 0 a 23!")

# Exercicio 3 
nome = input("Digite seu nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print("seu nome é muito curto")
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print("Seu nome é longo")