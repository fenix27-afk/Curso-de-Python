# Forma ERRADA DE REPETIR ALGO
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5


print(n1)
print(n2)
print(n3)
print(n4)
print(n5)


# Forma CERTA DE REPETIR ALGO FOR
print('===== REPETICAO COM FOR ====')


for i in range(5):
    print(F'Numero: {i}')


print('=== Contar ate 50 de 2 em 2 ===')


for i in range(1,50,2):
    print(F'Numero: {i}')


print('=== Perguntar varias vezes algo ===')


qtd_pessoas = int(input('Quantas pessoas voce quer cadastrar'))
for i in range(qtd_pessoas):
    nome = input('Qual seu nome? ')
    print(f'Ola {nome}')


# Exemplo - Tabuada do 9
# Pensar na contagem
for i in range(11):
    resultado = i * 9
    print(f'{i} * {9} = {resultado}')

# # Pergunte ao usuario a tabuada de um numero e ate quanto ele quer

for i in range(10):
    print(f'Numero {i+1}')

numero = int(input('Deseja tabuada de qual numero? '))
vezes = int(input('Deseja ir ate quanto? '))

for i in range(vezes+2):
    multiplicacao = 1 * numero
    print(f'(1) x {numero} = {multiplicacao}') 