import json

filename = 'users.json'
nome = input('qual é seu nome?')

with open(filename, 'w') as arquivo:
    json.dump(nome, arquivo)
    print(f'nós lembraremos de você {nome}')
    