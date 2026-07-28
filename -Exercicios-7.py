# Validação de acesso
# Um sistema precisa verificar duas informações:
# Se o usuário possui cadastro.
# Se a senha está correta.
# Crie um programa que receba essas informações e utilize o operador lógico
# AND .

cadastro = input('Usuario possui cadastro? (S/N)')
senha = input('Senha está correta: (S/N)')
validacao = (cadastro == 'S' ) and (senha == 'S' or senha == 'S' )

print('------------------------------------')

print(f'Resultado da validção: {validacao}')
