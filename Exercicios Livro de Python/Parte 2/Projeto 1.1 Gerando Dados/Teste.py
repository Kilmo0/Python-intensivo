from random import choice
import matplotlib.pyplot as plt 

class randomwalk():
    def __init__(self, pontos=5000):
        self.pontos = pontos
        self.valorx = [0]
        self.valory = [0]

    def fillwalk(self):
        while len(self.valorx) < self.pontos:
            directionx = choice([1, -1])
            distancex = choice([0, 1, 2, 3, 4])
            stepx = directionx * distancex

            directiony = choice([1, -1])
            distancey = choice([0, 1, 2, 3, 4])
            stepy = directiony * distancey

            if stepx and stepx == 0:
                continue
            
            nextx = self.valorx[-1] + stepx
            nexty = self.valory[-1] + stepy

            self.valorx.append(nextx)
            self.valory.append(nexty)

rw = randomwalk()
numpontos = list(range(rw.pontos))

while True:

    rw.fillwalk()
    plt.scatter(rw.valorx, rw.valory, s=15, c=numpontos, cmap=plt.cm.Blues, edgecolors=None)
    plt.show()
    msg = input('Deseja fazer uma nova simulação? Y/N ')
    if msg == 'N':
        break

print(numpontos)