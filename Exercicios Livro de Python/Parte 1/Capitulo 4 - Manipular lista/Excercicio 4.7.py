"""
4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista.
"""

multres = []
for multi in range(1,11):
    mul3 = multi * 3
    multres.append(mul3)
print(multres)