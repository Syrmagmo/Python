"""
- Criar variaveis para nome (srt), idade(int)
- altura (float), e peso (float) de uma pessoa 
- Criar variavel com o ano atual (int)
- obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
- obter o IMC da pessoa com 2 casa decimais (peso e na altura da pessoa)
- exibir um texto com todos os valores na tela usando F-String (com as chaves)

"""
nome = 'Lincoln'
idade = 20
altura = 1.77
peso = 92.00
imc = peso / altura ** 2
ano_atual = 2022
nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} esta em {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')