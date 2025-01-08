"""
5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir que a
lista de usuários não esteja vazia.
•  Se  a  lista  estiver  vazia,  mostre  a  mensagem  Precisamos  encontrar  alguns
usuários!
•  Remova  todos  os  nomes  de  usuário  de  sua  lista  e  certifique-se  de  que  a
mensagem correta seja exibida.
"""

Usuario = 'Madalena'
Users = []

if Users:
    if Usuario == 'Admin' and Usuario in Users:
        print('Olá Admin, Gostaria de ver o relatório diario?')
    elif Usuario in Users:
        print('Olá {} seja bem vindo!'.format(Usuario.title()))
    else:
        print('Olá {} não foi encontrado seu usuário'.format(Usuario.title()))
else:
    print('Não há usuarios no nosso programa ')