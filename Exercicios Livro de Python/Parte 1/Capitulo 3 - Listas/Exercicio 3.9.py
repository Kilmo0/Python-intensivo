"""
Trabalhando  com  um  dos  programas  dos
Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma mensagem
informando o número de pessoas que você está convidando para o jantar.
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
        
#descobrindo que não vai chegar a mesa a também
fisac = convidados.pop(0)
fnicolas = convidados.pop(0)
fjesus = convidados.pop(0)
fleonardo = convidados.pop(1)
feinsten = convidados.pop(1)
fAmanda = convidados.pop(1)

falta = [fisac, fnicolas, fjesus, fleonardo, feinsten, fAmanda]

#para os que não serão mais convidados
for faltante in falta:
    print('boa tarde {} infelizmente a nova mesa não chagará, então estaremos infelizmente te removendo do evendo, mas não se preocupe \nnós te convidaremos para outro evendo\n\n\n Ass: Kauã Lorenzi'.format(faltante.title()))

#para o que ainda serão convidados
for convidado in convidados:
    print('boa tarde {}, lembrando que vocês ainda estão convidados para nosso evento'.format(convidado.title()))

#deletando pessoas
del fAmanda
del feinsten

#numero de convidados
print(len(convidados))