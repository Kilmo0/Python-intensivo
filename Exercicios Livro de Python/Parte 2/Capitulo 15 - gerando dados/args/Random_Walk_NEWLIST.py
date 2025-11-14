from random import choice

class randonwalk:
    def __init__(self, numeros_pontos=100):
        self.numeros_pontos = numeros_pontos
        self.eixo_X = [0]
        self.eixo_Y = [0]

    def fillwalk(self):
        while len(self.eixo_X) < self.numeros_pontos:
            mover_X = choice([0, 1, 2, 3, 4])
            mover_Y = choice([0, 1, 2, 3, 4])

            Distancia_X = choice([0, 1, 2, 3, 4])
            Distancia_Y = choice([0, 1, 2, 3, 4])

            Total_x = mover_X * Distancia_X
            Total_y = mover_Y * Distancia_Y

            if Total_x and Total_y == 0:
                continue

            proximo_X = self.eixo_X[-1] + Total_x
            proximo_Y = self.eixo_Y[-1] + Total_y
            self.eixo_X.append(proximo_X)
            self.eixo_Y.append(proximo_Y)


