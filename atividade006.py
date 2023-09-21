"""Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Olá, qual o horário atual? ')

try:
    hora = int(horario)

    if hora >= 0 and hora <= 11:
        print('Obrigado, bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Obrigado, boa tarde!')
    elif hora >= 18 and hora <= 24:
        print('Obrigado, boa noite!')
    else:
        print('Não conheço essa hora')

except:
    print('Digite apenas númeors inteiros')