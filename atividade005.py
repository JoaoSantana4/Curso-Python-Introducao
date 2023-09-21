"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.


numero_digitado = int(input('Digite um número inteiro: '))

if numero_digitado:
    par_impar = numero_digitado % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {numero_digitado} é {par_impar_texto}')

else:
    print('Você não digitou um número inteiro')
    """



numero_digitado = int(input('Digite um número inteiro: '))

try:
    par_impar = numero_digitado % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar: #poderia colocar "if par_impar is True ou par_impar == True"
        par_impar_texto = 'par'

    print(f'O número {numero_digitado} é {par_impar_texto}')

except:
    print('Você não digitou um número válido')