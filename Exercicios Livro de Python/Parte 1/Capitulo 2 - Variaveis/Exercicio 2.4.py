#letra maisculas e minusculas em nomes
#Armazene nome de uma pessoa em uma variavel e apresente o nome dessa pessoa em letras maisculas minuscula e somente a primeira pessoa minuscula

#introdução/complementos
print('bom dia tudo certo? poderia me dizer seu nome?')
nome = input()

#utilizando o codigo
print('o seu nome  é kaua')
print('o seu em maisculo é {}'.format(nome.upper()))
print('seu nome em minusculo é {}'.format(nome.lower()))
print('e seu nome somente com a primeira letra maicula é {}'.format(nome.title()))

#também poderiamos usar o comando
#print('a variação maiscula minuscula e somente com a primeira letra maiscula do seu nome é: {}, {}, {},'.format(nome.upper(), nome.lower(), nome.title()))