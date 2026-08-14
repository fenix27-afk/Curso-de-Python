# E com outro for mestre os produtos cadastrados.
produtos = []

for i in range(3):
    produto = input('Deseja cadastrar qual prduto:')
    produtos.append(produto)

print('\n')
print('===== PRODUTOS CADASTRADOS =====')

for i in produtos:
    print(i)
    