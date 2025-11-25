from random import randint
import pygal

class dice:
    def __init__(self, num_lados):
        self.num_lados = num_lados
    
    def rolar(self):
        return randint(1, self.num_lados)
    
    def rolar_eixos(self, num_vezes):
        lista = []
        for i in range(1, num_vezes + 1):
            lista.append(self.rolar())
        return lista
    
    def contar(self, lista):
        novalist = []
        for i in range(1, self.num_lados + 1):
            novalist.append(lista.count(i))
        return novalist
    
total = dice(16)
dado1 = dice(8)
dado2 = dice(8)
dado1_1ktimes = dado1.rolar_eixos(1000)
dado2_1ktimes = dado2.rolar_eixos(1000)
ambos = dado1_1ktimes + dado2_1ktimes
templist = []
for a, b in zip(dado1_1ktimes, dado2_1ktimes):
    temp = a + b
    templist.append(temp)
ambas = total.contar(templist)
print(ambas)


graph = pygal.Bar()
graph.title = "2 Dados"
graph.x_labels = list(range(2, 17))
graph._x_title = "Resultado"
graph.add("Dado", total.contar(templist))
graph.render_to_file("Ex6.svg")

