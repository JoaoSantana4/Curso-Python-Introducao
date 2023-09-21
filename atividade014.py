import sys

cpf_enviado = input('DIGITE O SEU CPF PARA VALIDAÇÃO: ')

verificaçao = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)
if verificaçao:
    print('VOCÊ NÃO ENVIOU DADOS SEQUENCIAIS')
    sys.exit()

nove_digitos = cpf_enviado[:9]
contador_regresivo_1 = 10

resultado_dig1 = 0
for digito in nove_digitos:
    resultado_dig1 += int(digito) * contador_regresivo_1
    contador_regresivo_1 -= 1
digito_1 = ((resultado_dig1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = cpf_enviado[:10]
contador_regresivo_2 = 11

resultado_dig2 = 0
for digito in dez_digitos:
    resultado_dig2 += int(digito) * contador_regresivo_2
    contador_regresivo_2 -= 1
digito_2 = ((resultado_dig2 * 10) % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é válido')
else:
    print('CPF inválido')