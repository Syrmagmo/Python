"""
operadores lógicos 
AND, OR , NOT
in e not in

"""
# (verdadeiro e false) = falso
comparacao = 0
comparacao1 = 0

comparacao1 and comparacao


a = 2 
b = 3 

if b > a:
     print('B e maior do que A')
else:
    print('A e maior que B')
    


a = "adsfasdf"
b = 0 

if not b:  # If not, caso o valor for 0 ou nullo utilizar not
    print('Por favor, preencha o valor de B.')  

nome = "lincoln Richard"
if 'k' in nome:  #In se possui dentro de nome executa o proximo print
    print("Existe")
else:
    print("não existe")
    

nome = "lincoln Richard"
if 'k' not in nome:  #Já o Not in, caso NÃO exista dentro de nome ele irar imprimir o proximo print 
    print("Executei.")
else:
    print("Existe o texto")