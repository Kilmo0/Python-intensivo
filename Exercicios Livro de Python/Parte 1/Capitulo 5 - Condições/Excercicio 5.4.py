"""
5.4 – Cores de alienígenas #2: Escolha uma cor para um alienígena, como foi
feito no Exercício 5.3, e escreva uma cadeia if-else.
• Se a cor do alienígena for verde, mostre uma frase informando que o jogador
acabou de ganhar cinco pontos por atingir o alienígena.
•  Se  a  cor  do  alienígena  não  for  verde,  mostre  uma  frase  informando  que  o
jogador acabou de ganhar dez pontos.
• Escreva uma versão desse programa que execute o bloco if e outro que execute
o bloco else
"""

alien_color = 'Amarelo'

if alien_color == 'verde':
    print('Parabéns! você ganhou 5 pontos')
else:
    print('Parabéns! você acabou de ganhar 10 pontos')

alien_color = 'verde'

if alien_color == 'verde':
    print('Parabéns! você ganhou 5 pontos')
else:
    print('Parabéns! você acabou de ganhar 10 pontos')