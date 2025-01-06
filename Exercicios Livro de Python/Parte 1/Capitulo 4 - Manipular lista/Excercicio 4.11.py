"""
4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte:
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
•  Prove  que  você  tem  duas  listas  diferentes.  Exiba  a  mensagem  Minhas  pizzas
favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a
mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço
for  para  exibir  a  segunda  lista.  Certifique-se  de  que  cada  pizza  nova  esteja
armazenada na lista apropriada.
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