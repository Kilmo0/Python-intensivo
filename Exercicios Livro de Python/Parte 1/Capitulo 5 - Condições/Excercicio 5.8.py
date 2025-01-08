"""
5.8 – Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo o
nome 'admin'. Suponha que você esteja escrevendo um código que exibirá uma
saudação a cada usuário depois que eles fizerem login em um site. Percorra a lista
com um laço e mostre uma saudação para cada usuário:
• Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo,
Olá admin, gostaria de ver um relatório de status?
• Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por
fazer login novamente
"""

Usuario = 'Maladona'
Users = ['Admin', 'Kauã', 'Amanda', 'Brian', 'Allan']

if Usuario == 'Admin' and Usuario in Users:
    print('Olá Admin, Gostaria de ver o relatório diario?')
elif Usuario in Users:
    print('Olá {} seja bem vindo!'.format(Usuario.title()))
else:
    print('Olá {} não foi encontrado seu usuário'.format(Usuario.title()))