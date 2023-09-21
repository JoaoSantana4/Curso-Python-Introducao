while True:
    inicio = input('VOCÊ QUER GERAR UM CPF? [s]im [n]ão: ')

    if inicio == 's':
        import random

        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0, 9))
        
        contador_regresivo_1 = 10

        resultado_dig1 = 0
        for digito in nove_digitos:
            resultado_dig1 += int(digito) * contador_regresivo_1
            contador_regresivo_1 -= 1
        digito_1 = ((resultado_dig1 * 10) % 11)
        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = nove_digitos + str(digito_1)
        contador_regresivo_2 = 11

        resultado_dig2 = 0
        for digito in dez_digitos:
            resultado_dig2 += int(digito) * contador_regresivo_2
            contador_regresivo_2 -= 1
        digito_2 = ((resultado_dig2 * 10) % 11)
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

        print(cpf_gerado)

    elif inicio == 'n':
        print('OK')

    else:
        print('POR FAVOR DIGITE s OU n')
        continue