# Exercício: Números e seus quadrados
# Crie um programa que peça ao usuário 5 números inteiros.

quadrados = []
soma_quadrados = 0

for i in range(5):
  numero = int(input('Digite um numero: '))
  quadrado = numero ** 2
  quadrados.append(quadrado)

for i in quadrados:
  soma_quadrados = soma_quadrados + i

print(F'A soma dos quadrados é: {soma_quadrados}')