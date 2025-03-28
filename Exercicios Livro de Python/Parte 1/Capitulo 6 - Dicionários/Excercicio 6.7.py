"""
6.1 – Pessoa: Use um dicionário para armazenar informações sobre uma pessoa
que  você  conheça.  Armazene  seu  primeiro  nome,  o  sobrenome,  a  idade  e  a
cidade em que ela vive. Você deverá ter chaves como first_name,  last_name,
age e city. Mostre cada informação armazenada em seu dicionário
"""

pessoa1 = {
    'nome': 'Kauã Lorenzi', 
    'Idade': '19',
    'Cidade': 'Timbó'
}
pessoa2 = {
    'nome': 'Brian Fernando', 
    'Idade': '32',
    'Cidade': 'Timbó'
}
pessoa3 = {
    'nome': 'Allan kipfer', 
    'Idade': '30',
    'Cidade': 'Timbó'
}

people = [pessoa1, pessoa2, pessoa3]

for userinfo in people:
    print(f'Olá meu é {userinfo['nome']}, tenho {userinfo['Idade']} anos e nasci em {userinfo['Cidade']}')