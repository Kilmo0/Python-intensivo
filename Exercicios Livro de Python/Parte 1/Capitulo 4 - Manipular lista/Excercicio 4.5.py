""" 
4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em
seguida, use min() e max() para garantir que sua lista realmente começa em um e
termina em um milhão. Além disso, utilize a função sum() para ver a rapidez com
que Python é capaz de somar um milhão de números.
"""

#lista
numeros = []

#colocando numero de 1 a 1000000
for numero in range(1,1000001):
    numeros.append(numero)

#contagem
print(max(numeros))
print(min(numeros))

#no caso isso faz a soma dos numeros naturais, não do factorial
print(sum(numeros))