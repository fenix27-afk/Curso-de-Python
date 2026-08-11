# importando funcao random
import random

numero_secreto = random.randint(1,20)
tentativas = 5

while tentativas >= 1:
    chute = int(input('Chute um numero inteiro: '))
    tentativas -= 1
    if chute == numero_secreto:
        print('Parabens, voce acertou!')
        break

    if chute == numero_secreto:
        print('Parabens, voce acertou!')
        break

    if chute > numero_secreto:
        print('Numero secreto é menor')
    else:
        print('Numero secreto é maior')
    

    print(f'Voce tem {tentativas} tentativas')
else:
    print('GAME OVEEEERRRR - BOOT')
    print(F'O numero secreto é: {numero_secreto}')






 
