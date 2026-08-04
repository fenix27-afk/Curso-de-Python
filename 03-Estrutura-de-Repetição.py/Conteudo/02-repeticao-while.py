# Exemplo while
contador = 1

print('=== incremento ===')
while contador <= 8:
    print(contador)
    contador += 1 # Incremento (adicionando +1)

# decremento
print('=== decremento ===')
contador2 = 9

while contador2 >= 1:
    print(contador2)
    contador2 -= 1

    # Interrupcao
    print('=== InTERRUPÇÃO ===')
i = 1
while i <= 12:
    print(i)
    if i == 10:
        break
    i += 1

# Continue
print('=== COONTINUE ===')
e = 0
while e < 10:
    e += 1
    if e == 4:
        continue

    print(e)

# else
print('==== ELSE ===')
r = 1
while r < 6:
    print(r)
    r += 1
else:
    print('Condição deu falso')




