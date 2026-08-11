contador = 0 

while contador < 10:
    itens = int(input('Digite a quantidade de itens: '))


    if contador + itens > 10:
        print('Quantidade excedeu o limite')
        break

    if itens<= 0:
        print("quantidade invalida!")
        continue


    contador = contador + itens
    print(f'A quantidade acumulada foi de {contador}')
