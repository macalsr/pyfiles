PA = float(input('Preço de mercado concorrente A => '))
PercA = float(input('Participação de mercado concorrente A % => '))
PB = float(input('Preço de mercado concorrente B % =>'))
PercB =  float(input('participação de mercado concorrente B% => '))
PC = float(input('Preço do mercado concorrente C => '))
PercC = float(input('Participação de mercado concorrente C % => '))
PS = float(input("Preço sugestão => "))

#Cáculo do valor médio de mercado
VMM = PA*(PercA/100) + PB*(PercB/100) + PC*(PercC/100)
print('Valor de mercado: R$',VMM)

if PS>VMM:
    DIF= PS-VMM
    print('Seu preço de venda está excessivo em relação ao mercado')
    print('Margem ultrapassa, em reais', DIF)
    print('Entre com nova sugestão de preço')
else:
    DIF = VMM-PS
    print("PARABÉNS. Seu preço de vend esta competitivo em relação ao mercado")
    print('Margem disponivel em reais: ', DIF)