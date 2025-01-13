"""
6.1 – Pessoa: Use um dicionário para armazenar informações sobre uma pessoa
que  você  conheça.  Armazene  seu  primeiro  nome,  o  sobrenome,  a  idade  e  a
cidade em que ela vive. Você deverá ter chaves como first_name,  last_name,
age e city. Mostre cada informação armazenada em seu dicionário
"""

pessoa = {
    'nome': 'Kauã Lorenzi', 'Idade': '19', 'Cidade': 'Timbó'
}

print('Olá, meu nome é {} tenho {} de idade e eu nasci em {}'.format(pessoa['nome'], pessoa['Idade'], pessoa ['Cidade']))