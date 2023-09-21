entrada = input('[E]ntrar [S]air: ' )
senha_digitada = input('Digite a senha de acesso: ')

senha_acesso = '12345'

if entrada == 'E' and senha_digitada == senha_acesso:
    print('Você Entrou no Sistema')
elif entrada == 'S' and senha_digitada == senha_acesso:
    print('Você saiu do Sistema')
else:
    print('ERRO')