"""
4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços
for  para  fazer  exibições  a  fim  de  economizar  espaço.  Escolha  uma  versão  de
foods.py e escreva dois laços for para exibir cada lista de comidas.
"""

#fazendo a lista
pizzas = ['4 queijos', 'frango', 'lombinho']

#adiciando o laço mais a mensagem
for pizza in pizzas:
    print('eu gosto muito de pizza sabor {}'.format(pizza.title()))

#3 mensagens fora o laço 
print('pizza não é somente um sabor é uma paixão')
print('pizza pizza são gostosas')
print('eu realmente gosto de pizza')

#adicionando uma lista para meu amigo
pizzaamigo = pizzas[:]

#adicionando nova pizza
pizzas.append('margarita')


#adicionando para meu amigo
pizzaamigo.append('doritos')

#provando ser duas listas diferentes
print(pizzas)
print(pizzaamigo)

#criando laço
for pizzaa in pizzaamigo:
    print('meu amigo gosta muito da pizza {}'.format(pizzaa.title()))
#criando mais um laço
for pizz in pizzas:
    print(pizz)