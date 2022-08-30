#Mini-game, Forca

secreto = 'perfume'
digitadas = []
chances = 3 

while True:
    
    if chances <= 0:
        print('Você perdeu!!!')
        break
    
    letra = input("Digite uma letra: ")
    
    if len(letra) > 1:
        print("Ahhhhhh isso não vale, Digite apenas uma letra.")
        continue
    
    digitadas.append(letra)  #Para armazenar dados digitados pelo usuario
    
    if letra in secreto:
        print(f'Uhullllll, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f"AFFFZZ: a letra '{letra}' Não existe na palavra secreta.")
        digitadas.pop()  #para apagar o ultimo elemento
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'  #Para exibir os *** no lugar das letraras ocultas
  
    if secreto_temporario == secreto:
        print(f'Que legal, você ganhou!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f"A palavra secreta está assim: {secreto_temporario}")
    
    if letra not in secreto:
        chances -= 1
    
    print(f"Você ainda tem {chances} chances.")
    print()