Magicos = ['Ivan', 'Ox', 'Karl', 'Rubick']
losmagos = []

def mostrar_nome(lista):
    print('o nome dos mágicos são:')
    for nome in lista:
        print(nome)

def O_grande(lista, novalista):
    for nome in lista:
        nomegrande = f'{nome.title()} o grande'
        print(nomegrande)
        novalista.append(nomegrande)

O_grande(Magicos, losmagos)

print(losmagos)