nome = 'lincoln'
idade = 20
altura = 1.77
peso = 92
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc e', imc)  

print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')  #Coloacando o F na frente podese formatar com {} no lugar da , fincando mais pratico e bonito no codigo
print('{} tem {} anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))  # Outra forma de formatar 
print('{0} tem {1} {0} anos de idade e seu imc e {0} {2:.2f}'.format(nome, idade, imc))  #Numerando as celulas pode se repetir sem que a ordem altere os fatores
print('{n} tem {i} anos de idade e seu imc e {im:.2f}'.format(n=nome, i=idade, im=imc))  #Nomenado as celulas pode ser editado como desejar sem erros