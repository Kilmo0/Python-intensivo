import matplotlib.pylab as plt

#dados
valorx = list(range(1, 5001))
valory = [x**3 for x in valorx]

#titulo
plt.title("Valores ao cubo", fontsize=20)
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

#plot
plt.scatter(valorx, valory, c=valory, cmap=plt.cm.Purples, edgecolors='none', s=40)


plt.show()