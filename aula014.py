print('Olá, você está no SAC da empresa ROBERT BOSCH')

ajuda = input('Você deseja ser atendido por um dos nosso funcionários? Responda com "Sim" ou "Não": ')

if ajuda == 'Sim':
    print('Certo, iremos te enchaminhar para a fila de atendimento, aguarde.')

elif ajuda == 'Não':
    print('Ok, irei encerrar o atendimento.')

else:
    print('Ops, não entendi o que você quis dizer :/ ')