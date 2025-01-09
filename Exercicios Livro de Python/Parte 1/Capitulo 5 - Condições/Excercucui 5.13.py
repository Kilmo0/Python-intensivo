"""
5.13 – Suas ideias: A essa altura, você é um programador mais capacitado do
que era quando começou a ler este livro. Agora que você tem melhor noção de
como  situações  do  mundo  real  são  modeladas  em  programas,  talvez  esteja
pensando em alguns problemas que poderia resolver com seus próprios programas.
Registre qualquer ideia nova que tiver sobre problemas que você queira resolver à
medida que suas habilidades em programação continuam a melhorar. Considere
jogos que você queira escrever, conjuntos de dados que possa querer explorar e
aplicações web que gostaria de criar.
"""

Cadastrados = ['Kilmo', 'Texungo', 'Akpfer']
novoscadastros = ['Amanda Janke', 'Akpfer']

Cadastradoslow = [cadastrado.lower() for cadastrado in Cadastrados]
novoscadastroslow = [novos.lower() for novos in novoscadastros]

for cadastrados in novoscadastroslow:
    if cadastrados in Cadastradoslow:
        print('o Seu usuário já foi cadastrado {}'.format(cadastrados.title()))
    else:
        print('seja bem vindo {}'.format(cadastrados.title()))
        