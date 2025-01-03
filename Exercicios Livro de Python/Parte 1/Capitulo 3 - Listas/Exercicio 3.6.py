"""
3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior, portanto agora tem mais espaço disponível. Pense em mais três convidados para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista
"""

convidados = ['Jesus', 'Lucifer', 'leonardo da Vince', 'albert einsten', 'Amanda Janke']

faltou = convidados.pop(1)
convidados.insert(1, "Elon Musk")

#achei uma mesa maior
#for convidado in convidados:
#    print('olá {} espero que esteja tudo bem com você!\nacabamos de achar uma mesa maior portanto será convidados mais pessoas \ninfelizmente o {}, não irá comparacer\n\nAss: Kauã Lorenzi'.format(convidado.title(), faltou))

convidados.insert(0, "Isacc newton")
convidados.insert(1, 'Nicolas Tesla')
convidados.append('benjamin Franklin')

print('boa tarde a todos\nGostaria de anunciar que o {}, {} e {},\n também irão comparecer a nossa jantar para discutimos'.format(convidados[0], convidados[1], convidados[-1]))
for convidado in convidados:
    print('Boa tarde {},\ngostaria de te convidar para um jantar para discutirmos\ninfelizmente o {} não irá comparecer, devido a problemas técnicos\nagradeço a comprenção\n\n\n\tAss: Kauã Lorenzi\n'.format(convidado.title(), faltou))
        