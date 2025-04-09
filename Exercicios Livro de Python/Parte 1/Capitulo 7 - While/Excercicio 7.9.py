pães = ['Atum', 'Ovo', 'carne', 'Misto quente', 'Peito de peru', 'Atum', 'Atum']

terminados = []

for pão in pães:
    print(f'preparei um sandwiche de {pão}')
    terminados.append(pão)

print('todos os sandwiches foram terminados\n')

while 'Atum' in terminados:
    terminados.remove('Atum')


for sandwiches in terminados:
    print(f'Sandwiche de {sandwiches}')
