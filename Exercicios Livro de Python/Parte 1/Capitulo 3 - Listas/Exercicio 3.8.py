"""
3.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que
você gostaria de visitar.
• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em
ordem alfabética.
• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
elegante; basta exibi-la como uma lista Python pura.
• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista
propriamente dita.
• Mostre que sua lista manteve sua ordem original exibindo-a.
• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a
ordem da lista original.
• Mostre que sua lista manteve sua ordem original exibindo-a novamente.
• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
que sua ordem mudou.
• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para
mostrar que ela voltou à sua ordem original.
•  Utilize  sort()  para  mudar  sua  lista  de  modo  que  ela  seja  armazenada  em
ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
•  Utilize  sort()  para  mudar  sua  lista  de  modo  que  ela  seja  armazenada  em
ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou
"""
#lista de locais para viajar
viagem = ['kiev', 'gramado', 'Fernando', 'jalapão', 'varsovia']

#exibir a lista em ordem alfabética
print(sorted(viagem))

#exibindo lista oroginal
print(viagem)

#exibindo lista ao contrario sem alterar a original
print(sorted(viagem, reverse=True))

#mostrando novamente que a lista manteve a ordem original (acho que eu poderia colocar letra maisculas)
print(viagem)

#invertendo a lista
viagem.reverse()
print(viagem)

#invertendo a lista ctrl+alt+baixo
viagem.reverse()
print(viagem)

#colocando em ordem alfabética
viagem.sort()
print(viagem)

#colocando em ordem alfabética inversa
viagem.sort(reverse=True)
print(viagem)