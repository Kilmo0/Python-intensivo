from die import die
import matplotlib.pylab as plt

die = die()

eixo1 = []
for i in range(100):
    tmp = die.rolls()
    eixo1.append(tmp)


frequencia = []
for i in range(1, die.num_sides+1):
    tmp = eixo1.count(i)
    frequencia.append(tmp)

print(eixo1)
print(frequencia)
