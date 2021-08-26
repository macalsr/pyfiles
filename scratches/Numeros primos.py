from math import sqrt

print('Primos: 2')
c, p, primos, limite = 1, 1, [2, ], 20

for numero in range(3, limite + 1, 2):
    ehprimo = 1
    for i in primos:
        c += 1
        if numero % i == 0:
            ehprimo = 0
            break
        if i > sqrt(numero):
            break
    if ehprimo:
        primos.append(numero)
        print(numero)
        p += 1

print('\n \n Foram encontrados %d numeros primos.' % p)
print('Foram necessárias %d comparações.' % c)
