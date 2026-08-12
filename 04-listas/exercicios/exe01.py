# Calcule a média das notas e mostre no print.
notas = [5.5, 8, 9.2, 5 ]
nota1 = notas[0] # 5.5
nota2 = notas[1] # 8
nota3 = notas[2] # 9.2
nota4 = notas[3] # 5
medio = (nota1 + nota2 + nota3 + nota4) 

quantidade_total_notas = len(notas)
media = (nota1 + nota2 + nota3 + nota4) / quantidade_total_notas

print(f'A média é de {round(media,2)}')
