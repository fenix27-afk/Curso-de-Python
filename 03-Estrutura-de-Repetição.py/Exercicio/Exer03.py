saldo = 10
while saldo > 0:
    saque = float(input('eseja sacar quanto? (0 para encerrar o atendimento)'))

    if saque == 0:
        print('Saldo indisponivel')
        break

    if saque > saldo:
        print("Atendimento encerrado")
        continue

    saldo = saldo - saque
    print(f'Saldo restante {round(saldo,2)}')

print('programa encerrado')






