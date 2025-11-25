from die import die
import pygal

die1 = die()
die2 = die(10)

eixo1 = []
for i in range(5000000):
    tmp = die1.rolls() + die2.rolls()
    eixo1.append(tmp)


frequencia = []
res_max = die1.num_sides + die2.num_sides
for i in range(2, res_max+1):
    tmp = eixo1.count(i)
    frequencia.append(tmp)


hist = pygal.Bar()
hist.title = "Resultado de 1000"
hist.x_labels = list(range(2, 17))
hist._x_title = "Resultado"
hist._y_title = "Frequencia do resultado"

hist.add('D6', frequencia)
hist.render_to_file('Die_Visual.svg')