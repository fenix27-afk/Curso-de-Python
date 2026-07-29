# Permite varias condicoes
# nota = float(input('Digite sua nota: '))

# if nota >= 7:
#     print('Aprovado')
# elif nota >= 5:
#     print('recuperacao')
# else:
#     print('Reprovado')

# print('======= EXEMPLO ======')
# idade = int( input('Digite sua idade:'))

# menor que 12 - crianca
# menor que 18 - adolescente
# menor que 60 - adulto
# melhor idade 

#  if idade < 12:
#     print('crianca')
#  elif idade < 18:
#     print('adolescente')
#  elif idade < 60:
#     print('adulto')
#  else:
#     print('melhor idade')

print('====== EXEMPLO - operador logico ======')

usuario = input('Possui cadastro? (S/N): ') .upper()
senha = input('Senha correta? (S/N): ') .upper()

if usuario == 'S' and senha == 'S':
    print('Acesso liberado')
else:
    print('Acesso negado')


    


