import matplotlib.pylab as plt

#dados
valorx = list(range(1, 5001))
valory = [x**3 for x in valorx]

plt.plot(valorx, valory)
plt.title("Valores ao Cubo", fontsize=20)
plt.xlabel("Valor do Eixo X", fontsize=12)
plt.ylabel("Valor do Eixo Y", fontsize=12)
plt.show()

