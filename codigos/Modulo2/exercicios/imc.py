"""
Calcule o imc de uma pessoa
"""
nome = 'Lincoln' 
idade = 20
altura = 1.77
peso = 92
maior18 = idade > 18
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)