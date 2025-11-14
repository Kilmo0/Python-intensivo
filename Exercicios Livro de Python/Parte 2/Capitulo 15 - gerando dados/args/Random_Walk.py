import matplotlib.pylab as plt
from random import choice

class randon_w():
    def __init__(self, num_points):
        self.num_points = num_points
        self.valorx = [0]
        self.valory = [0]

    def fillwalk(self):
        while len(self.valorx) < self.num_points:
            direcao_x = choice([1, -1])
            distancia_x = choice([0, 1, 2, 3, 4])
            xmov = direcao_x * distancia_x
            
            direcao_y = choice([1, -1])
            distancia_y = choice([0, 1, 2, 3, 4])
            ymov = direcao_y * distancia_y

            #reijeitar valor caso ambos sejam nulos
            if xmov == 0 and ymov == 0:
                continue
            
            #calcula proximos valores
            proximo_x = self.valorx[-1] + xmov
            proximo_y = self.valory[-1] + ymov
            self.valorx.append(proximo_x)
            self.valory.append(proximo_y)


