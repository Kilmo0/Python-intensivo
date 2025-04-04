active = True

print('bom dia, seja bem vindo a pizzaria')

mensagem = 'Por favor digite os igridientes que desejas\n'
mensagem += 'por favor caso deseja "sair" digite "sair"\n'

pizza = []

while active:
    info = input(mensagem)
    if info != 'sair':
        pizza.append(info)
    else:
        active = False
print(f'Sua pizzas possue seguintes sabores: {", ".join(pizza)}')