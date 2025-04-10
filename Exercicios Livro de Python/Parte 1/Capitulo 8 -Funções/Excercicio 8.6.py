def location(cidade, estado):
    local = {'cidade': cidade, 'pais': estado }
    return local

active = True

while active:
    print('digite "sair" para finalizar o programa')
    cidade = input('por favor digite uma cidade: ')
    if cidade == "sair":
        break
    país = input('por favor digite em qual pais essa cidade se localiza ')
    if país == "sair":
        active = False
    
    local = location(cidade, país)
    print(f'{local["cidade"]}, {local["pais"]}')
