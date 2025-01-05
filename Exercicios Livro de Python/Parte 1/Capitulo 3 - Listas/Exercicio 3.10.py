"""
3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
lista.  Por  exemplo,  você  poderia  criar  uma  lista  de  montanhas,  rios,  países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie
uma  lista  contendo  esses  itens  e  então  utilize  cada  função  apresentada  neste
capítulo pelo menos uma vez.
"""

#bora lá

#lista de criptomoedas
cryptos = ['Bitcoin', 'Ethereum', 'XRP', 'Cardano', 'Avax', 'Dogecoin', 'Solana']

#criando uma mensagem para cada item
for cripto in cryptos:
    print('Hoje eu comprei {} a mais'.format(cripto)) 

#Excluindo um item
Fethereum = cryptos.pop(1)
print('Deixei de comprar', Fethereum)

#colocando uma moeda
cryptos.insert(1, 'BNB')
print(cryptos)

#deletando 1 elemento
cryptos.remove('Dogecoin')
print(cryptos)

#colocando em ordem alfabética permanente
cryptos.sort()
print(cryptos)

#colocando em ordem alfabética reversa permanente
cryptos.sort(reverse=True)
print(cryptos)

#colocando em ordem alfabética
print(sorted(cryptos))

#colocando em ordem alfabética reversa
print(sorted(cryptos, reverse=True))

