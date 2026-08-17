# importando funcao random
import random

numero_secreto = random.randint(1,150)
tentativas = 1

print('==== VOCE TERA CINCO TENTATIVAS ====')
while tentativas <= 5:
    chute = int(input('Chute um numero entre 1 e 150: '))

    if chute == numero_secreto:
        print('Parabens, voce acertou!')
        break

    if chute > numero_secreto:
        print('Numero secreto é menor')
    else: 
        print('Numero secreto é maior')

    tentativas += 1
    print(f'Voce tem {tentativas} tentativas')
else:
    print('GAME OVERRRRRRR - NOOB')
    print(f'O numero secreto é: {numero_secreto}')