saldo = 10
while saldo > 0:
    saque = float(input('Deseja sacar quanto? (0 para encerrar o atendimento)'))

    if saque == 0:
        print("Atendimento encerrado")
        break

    if saque > saldo:
        print('Saldo indisponivel')
        continue

    saldo = saldo - saque
    print(f'Saldo restante {round(saldo,2)}')
else:
    print('Saldo Negativo')

print('Programa ecenrrado')

    