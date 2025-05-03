filename = 'nome'

nome = input('qual é seu nome?\n')

with open(filename, 'w', encoding='UTF-8') as arquivo:
    arquivo.write(nome)