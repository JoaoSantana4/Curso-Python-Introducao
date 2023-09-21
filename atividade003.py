'''Método 1 (lógica errada)

primeiro_valor = input('Digit um valor: ')
segundo_valor = input('Digite um valor: ')

condição = 'primeiro_valor' > 'segundo_valor'

if condição == True:
    print(f'o primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
else:
    print(f'o primeiro valor {primeiro_valor} é meneor que o primeiro valor {segundo_valor}')
    '''

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior ou igual do que segundo valor {segundo_valor}')

else:
    print(f'O segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}')