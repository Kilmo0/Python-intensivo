cripto = []

cripto.append('bitcoin')
cripto.append('ethereum')
cripto.append('cardano')

cripto.insert(0, "XRP")

nocripto = 'ethereum'
cripto.remove(nocripto)

for criptos in cripto:
    print(criptos)

print("{} não é uma criptomoeda".format(nocripto.title()))
