import matplotlib.pylab as plt


#dados
valoresx = list(range(1, 1000))
valoresy = [i**2 for i in valoresx]


#valores
plt.scatter(valoresx, valoresy, c=valoresy, cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.title("Numeros ao quadrado")
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Valor ao quadrado", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.show()