numero = 0
while numero <= 10:
    fat = 1
    fat_str = '1'
    for i in range(numero,0,-1):
        if i == numero:
            fat = numero
            fat_str = str(i)
        else:
            fat *= i
            fat_str = fat_str + '*' + str(i)
    print('Fatorial de %s: %s! = %s = %s' % (numero, numero, fat_str, fat))
    numero += 1