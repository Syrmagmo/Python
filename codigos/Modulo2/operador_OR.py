"""
Operador OR
"""
from calendar import c
from tkinter import E
from unittest.mock import NonCallableMagicMock


nome = input("Qual o seu nome? ")

if nome:
    print(nome)
else:
    print("Voce não digitou nada ='(" )
    
#--------------------------- Outra forma de fazer

print(nome or "Você não digitou nada")


#--------------------------- Outra forma de fazer

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = "Lincoln"

variavel = a or b or c or d or e or f or g  #Qual for verdadeiro primeiro ele ira parar
print(variavel)