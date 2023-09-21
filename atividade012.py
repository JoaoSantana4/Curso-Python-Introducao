"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = [] #cria lista vazia

while True: #começa o loop
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor) #adciona o 'valor' para a lista
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice] #Deleta o indice escolhido da lista

        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

        #Esses excepts foram utilizados para captar erros

    elif opcao == 'l':

        if len(lista) == 0:
            print('Nada para listar') #Se não houver nada na lista, nada será listado

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')