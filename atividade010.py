palavra_secreta = 'joao' #declarei a palavra secreta
letras_corretas = ' '
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ') #pedi para o usuario colocar uma letra

    if len(letra_digitada) > 1: #verifico se o usuario digitou apenas 1 letra
        print('Digite apenas uma letra.')
        continue #se o usuario digitar mais do que 1 letra, mando ele para o inicio

    if letra_digitada in palavra_secreta:
        letras_corretas += letra_digitada #se a letra digitada estiver na palavra, eu coloco ela dentro da str "letras_corretas" que é uma str vazia
        numero_tentativas += 1

    palavra_formada = ""
    for letra_secreta in palavra_secreta: #construção da lógica para utilizar os *
        if letra_secreta in letras_corretas: #se a letra secreta estiver entre as letras que o usuario acertou 
            palavra_formada += letra_secreta  #somar a str vazia "palavra_formada" com a str "letra_secreta"
        else:
            palavra_formada += '*' #soma um * com a str vazia "palavra_formada"

    print('Palavra formada:', palavra_formada) #mostra a palavra de forma horizontal
    #quando chega aqui o loop termina e o programa volta para o while   

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS!')
        print(f'A PALAVRA ERA: {palavra_secreta}')  
        print(f'Você teve {numero_tentativas} tentativas')
        letras_corretas = ' '
        numero_tentativas = 0