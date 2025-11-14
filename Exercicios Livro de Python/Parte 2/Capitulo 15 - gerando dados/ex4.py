from args.Random_Walk_NEWLIST import randonwalk as rw
import matplotlib.pyplot as plt

rw = rw(5000)
rw.fillwalk()

valor = (list(range(rw.numeros_pontos)))

plt.scatter(rw.eixo_X, rw.eixo_Y, c=valor, cmap=plt.cm.Blues, s=5)
plt.show()

