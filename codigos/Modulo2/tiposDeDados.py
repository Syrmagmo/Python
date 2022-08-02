"""
Tipos de dados 
str - string - textos 'Assim' "Assim"
int  - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto - 10.50 1.5 -10.10 -50.93
bool - booleano/lóico - True/False 10 == 10

"""

print(type('Luiz'))  #Normalmente quando chamamos alguma coisa no print entre () estamos chamando uma classe ou uma função
#Type - Mostra o tipo se é string, int, bool, object etc.
print('10', type('10'))   #Numeros dentro das '' são tratadas como string
print(25.23, type(25.23))  #Utilizar o . ao inves de , em valores float
print('l' == 'L', type('l' == 'L'))  #False l não é igual a L
print(bool(''))  #Dara false, 0 também dará false

#           Type casting
print('luiz', type('luiz'), bool('luiz'))  #Convertendo para bool
print('10', type('10'), type(int('10')))  #Convertendo para int

#Casos em que não se pode realizar o Type Casting
print('luiz', int('luiz'))  # Erro
print('10.5', int('10.5'))  # Erro