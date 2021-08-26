controle = 1
while True:
    print('Mini Calculadora')
    print('1-Somar dois numeros')
    print('2-Subtrair dois numeros')
    print('3-Multiplicar dois numeros')
    print('4-Dividir dois numeros')
    print('5-Fatorial de um numero')
    print('6-potencia entre dois numeros')
    print('7-Sair')
    controle = int(input('Escolha uma opção: '))

    if controle == 7:
        break
    print('--------------------------------------', end='\n')

    if controle == 1:
        num_01 = float(input('Digite um numero: '))
        num_02 = float(input('Digite outro numero: '))
        print('\nA soma de', num_01, 'e', num_02, 'é', num_01 + num_02)
        print('--------------------------------------', end='\n')

    elif controle == 2:
        num_01 = float(input('Digite um numero: '))
        num_02 = float(input('Digite outro numero: '))
        print('\nA subtração de', num_01, 'e', num_02, 'é', num_01 - num_02)
        print('--------------------------------------', end='\n')

    elif controle == 3:
        num_01 = float(input('Digite um numero: '))
        num_02 = float(input('Digite outro numero: '))
        print('\nA multiplicação de', num_01, 'e', num_02, 'é', num_01 * num_02)
        print('--------------------------------------', end='\n')

    elif controle == 4:
        num_01 = float(input('Digite um numero: '))
        num_02 = float(input('Digite outro numero: '))
        if num_02 == 0:
            print('Não é possivel fazer divisão por 0')
            print('--------------------------------------', end='\n')
        else:
            print('\nA divisão de', num_01, 'e', num_02, 'é', num_01 / num_02)
            print('--------------------------------------', end='\n')

    elif controle == 5:
        num_01 = float(input('Digite um numero: '))
        fatorial = 1
        contador = num_01
        while contador > 1:
            fatorial *= contador
            contador -= 1
        print('\n O fatorial de', num_01, 'é', fatorial)
        print('--------------------------------------', end='\n')

    elif controle == 6:
        num_01 = float(input('Digite um numero: '))
        num_02 = float(input('Digite outro numero: '))
        print('\n', num_01, 'elevado a', num_02, 'é', num_01 ** num_02)
        print('--------------------------------------', end='\n')
