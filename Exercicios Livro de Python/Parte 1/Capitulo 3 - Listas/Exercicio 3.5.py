""""
3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar um
novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não poderá
comparecer.
•  Modifique  sua  lista,  substituindo  o  nome  do  convidado  que  não  poderá
comparecer pelo nome da nova pessoa que você está convidando.
•  Exiba  um  segundo  conjunto  de  mensagens  com  o  convite,  uma  para  cada
pessoa que continua presente em sua lista.
"""
convidados = ['Jesus', 'Lucifer', 'leonardo da Vince', 'albert einsten', 'Amanda Janke']

faltou = convidados.pop(1)
convidados.insert(1, "Elon Musk")


for convidado in convidados:
    print('olá {} espero que esteja tudo bem com você!\nvenho lhe convidar para um jantar para debater fatos Contamos muito sua presença \ninfelizmente o {}, não irá comparacer\n\nAss: Kauã Lorenzi'.format(convidado.title(), faltou))


