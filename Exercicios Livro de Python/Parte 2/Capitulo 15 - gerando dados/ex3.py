import matplotlib.pylab as plt
from args.Random_Walk import randon_w

rw = randon_w(5000)
rw.fillwalk()
pontos = list(range(rw.num_points))

#tamanho
plt.figure(dpi=128, figsize=(8, 6))

#plots
plt.plot(rw.valorx, rw.valory, linewidth=2)

#titulo 
plt.title("Simulador de Polem")
plt.xlabel("Valor X")
plt.ylabel("Valor y")


plt.show()