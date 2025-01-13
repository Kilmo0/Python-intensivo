"""
5.6  –  Estágios  da  vida:  Escreva  uma  cadeia  if-elif-else  que  determine  o
estágio da vida de uma pessoa. Defina um valor para a variável age e então:
• Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo
que ela é um bebê.
• Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem
dizendo que ela é uma criança.
• Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma mensagem
dizendo que ela é um(a) garoto(a).
e  a  pessoa  tiver  pelo  menos  13  anos,  mas  menos  de  20,  mostre  uma
mensagem dizendo que ela é um(a) adolescente.
•  Se  a  pessoa  tiver  pelo  menos  20  anos,  mas  menos  de  65,  mostre  uma
mensagem dizendo que ela é adulto.
• Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa
pessoa é idoso
"""

print('Digite aqui sua idade')
idade = int(input())

if idade <= 1:
    print('você é um bebe')
elif idade <= 3:
    print('você é uma criança')
elif idade <= 12:
    print('você é um garoto')
elif idade <= 19:
    print('você é um adolecente')
elif idade <= 64 :
    print('você é um adulto')
elif idade >= 65:
    print('você é idoso')
