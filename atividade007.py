"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".



MÉTODO 1 (MEU): 

nome = str(input('Digite seu nome e eu vou dizer se ele é grande ou pequeno: '))

letras_do_nome = len(nome)


try:
    if letras_do_nome <= 4:
        print('Seu nome é pequeno')
    elif letras_do_nome >= 5 and letras_do_nome <= 6:
        print('Seu nome é normal')
    elif letras_do_nome >= 7:
        print('Seu nome é grande')
    else:
        print('Digite um nome válido')

except:
   print('nome doido')

"""

#MÉTODO 2 (PROFESSOR)

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')