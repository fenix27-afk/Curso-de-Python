# Cadastro de usuario
# Crie um Programa que solicite informações de uma pessoa e depois exiba os dados cadastrados.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade:'))
cidade = input('Digite sua cidade:')
altura = float(input('digite sua altura:'))
carteira = input('Possui sua carteira de motorista? (S/N): ' )
possui_carteira = carteira == 'S' or carteira ==  's'


print('--- Dados do Usuário ---')


print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Cidade: {cidade}')
print(f'Altura: {altura}')
print(f'Possui carteira de motorista: {possui_carteira}')


