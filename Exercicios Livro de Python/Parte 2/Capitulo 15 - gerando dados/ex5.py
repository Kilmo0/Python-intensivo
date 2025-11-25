from random import randint
import pygal

class dice:
    def __init__(self, num_lados):
        self.num_lados = num_lados

    def rolar(self):
        return randint(1, self.num_lados)
    
    def rolar_eixo(self, num_ve):
        lista = []
        for i in range(1, num_ve + 1):
            lista.append(self.rolar())
        return lista
    
    def contar(self, lista):
        contar = []
        for i in range(1, self.num_lados+1):
            contar.append(lista.count(i))
        return contar



graph = pygal.Bar()
dado1 = dice(6)
dado1_100 = dado1.rolar_eixo(100)
print(dado1.contar(dado1_100))
graph.title = "Resultado de rotação"
graph.x_labels = list(range(1, 7))
graph._x_title = "Resultado"
graph._y_title = "Numero de vezes"
graph.add("Dado", dado1.contar(dado1_100))
graph.render_to_file("TEst.svg")