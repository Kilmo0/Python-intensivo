def make_pizza(tamanho, *ingredientes):
    #coloque primeiro o tamanho, depois os igredientes
    tamanho = str(tamanho)
    print(f'fazendo uma pizza {tamanho} cm')
    print('Ingredientes:')
    for sabor in ingredientes:
        print(f'- {sabor}')
    
