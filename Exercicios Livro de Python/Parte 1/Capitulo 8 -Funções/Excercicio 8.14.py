import time
from importacoes.Impressora import imprimir_modelos

active = True
lista = []

print('Digite "SAIR" para finalizar')
print('Digite "DEL" para deletar algum item')

while active:
    modelos = input('Digite o que deseja imprimir:\n')
    if modelos == 'SAIR':
        active = False
    elif modelos == "DEL":
        print('Digite o que queira deletar:')
        print(lista)
        modelodeletado = input()
        lista.remove(modelodeletado)
    else:
        lista.append(modelos)
        print(f'Objetos que serão impressso:\n{lista}')

imprimir = imprimir_modelos(lista)
