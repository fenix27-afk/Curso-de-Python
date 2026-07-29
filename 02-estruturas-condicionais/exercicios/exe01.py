# Crie um programa que solicite o peso a altura e mostre o IMC da pessoa

altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc = peso / altura ** 2

if imc  < 18.5:
    print('abaixo do peso normal') 
elif imc >= 18.5 and imc <= 24.9:
    print('Peso Normal')
elif imc >= 25.0 and imc <= 29.9:
    print('Excesso de peso')
elif imc >= 30.0 and imc < 34.9:
    print('Obesidade clase I')
elif imc >= 35.0 and imc <= 39.9:
    print('Obesidade clase II')
else:
    print('Obesidade clase III')
    
