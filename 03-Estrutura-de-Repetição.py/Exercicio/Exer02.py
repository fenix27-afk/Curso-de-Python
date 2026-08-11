# EXERCICIOS PRATICOS - WHILE

# saldo = 10
# while saldo <= 10:
#     print(saldo)
#     saldo =+ 1
#     saldo = 10
     

# i = 10
# while 1 <= 10:
#     print(1)
#     if 1 == 10:
#        break
#     i += 10

# e = 10
# while e < 10:
#     e += 1
#     if e == 10:
#         continue
#     print(e)

# r = 10
# while r < 10:
#     print(r)
#     r += 10

# else: 
#     print('Saldo em conta 0')

Saldo_Inicial = 500

print(f'Saldo Inicial: R$ {Saldo_Inicial: .2f}')

while Saldo_Inicial > 0:
    valor_saque = int(input('Voce deseja sacar quanto?:'))
    if valor_saque <= Saldo_Inicial:
        Saldo_Inicial -= valor_saque
    print(f'saldo_atual: R$ {Saldo_Inicial:.2f}')
    continue
else:
    print('Impossivel sacar, saldo abaixo do limite execivo')

