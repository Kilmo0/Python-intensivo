import matplotlib.pyplot as plt

lista1 = []; lista2 = []

for i in range(1, 6):
    i = i**3
    lista1.append(i)

for i in range(1, 6):
    lista2.append(i)

plt.plot(lista2, lista1, c='Blue')
plt.scatter(lista2, lista1, edgecolors=None)
plt.title('NUMEROS AO CUBO', fontsize=24)
plt.ylabel('Numeros ao Cubo', fontsize = 12)
plt.xlabel('Numeros', fontsize=12)
plt.tick_params(labelsize=14)
plt

plt.show()