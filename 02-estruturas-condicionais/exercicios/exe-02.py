# Um programa deve receber o comprimento dos três lados de um possível
# triângulo.
# Primeiro, verifique se os valores informados podem formar um triângulo.
# regra:
# A soma de dois lados deve ser maior que o terceiro.
# Depois:

# Se os três lados forem iguais: 
#  (Triângulo Equilátero)

# Se apenas dois lados forem iguais:
# (Triângulo Isósceles)

# Se todos os lados forem diferentes:
#  (Triângulo Escaleno)

Lado1 = float(input(' Lado Direito: '))
Lado2 = float(input(' Lado Esquerdo: '))
Lado3 = float(input(' Base: '))

if (Lado1 + Lado2 > Lado3) and (Lado2 + Lado3 > Lado1) and (Lado1 + Lado3 > Lado2):
    print('é um triangulo\n')

    if Lado1 == Lado2 == Lado3:
        print('Equilatero')
    elif Lado1 != Lado2 != Lado3:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os valores informados não formam um triangulo.')
