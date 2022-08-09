num1 = input("Digite um numero:  ")
num2 = input("Digite outro numero: ")

#num1 = int(num1)
#num2 = int(num2)

#print(num1 + num2)

#Temos que converter o input em um valor numerico mesmo quando o usuario digitar uma letra
#Como ? Com: isnumeric, isdigit isdecimal

#print(num1.isdecimal())
#print(num2.isdecimal())

#Maneira correta

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print("Digite apenas numeros, obrigado!")