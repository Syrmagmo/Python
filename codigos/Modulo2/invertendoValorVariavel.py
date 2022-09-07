


x = 10  # Lincoln
y = "lincoln"  #10

# X esta recebendo o valor de Y e o Y esta recebendo o valor de X
x,y = y,x

print(f"x={x}e y={y}")

z = "Richard"
x, y, z = z, x, y  # Os valores serao atribuindos em ordem EX; X = Z, Y = X,  Z = Y
print(f"x={x} e y={y} e z={z}")