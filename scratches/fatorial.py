numero = int(input('numero fatorial: '))

fatorial = 1
for termo in range(1, (numero + 1)):
    fatorial *= termo

print('fatorial de ' + str(numero) + '! é: ' + str(fatorial))