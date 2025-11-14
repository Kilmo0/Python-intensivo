from Random_Walk import randon_w
import matplotlib.pylab as plt

while True:
    rw = randon_w(50000)
    numeros_pontos = list(range(rw.num_points))
    rw.fillwalk()
    
    #tamanho
    plt.figure(dpi=128, figsize=(10, 8))
    
    #scatters
    plt.scatter(rw.valorx, rw.valory, c=numeros_pontos, cmap=plt.cm.Blues, s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.valorx[-1], rw.valory[-1], c='red', edgecolors='none', s=100)
    

    plt.show()
    rodando = input("Deseja continuar?")
    if rodando == 'n':
        break