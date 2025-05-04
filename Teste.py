import json

filename = 'users.json'

try:
    with open(filename) as arquivo:
        user = json.load(arquivo)
        print(user)
except FileNotFoundError:
    user = input('poderia nos dar seu nome?')
    with open(filename, 'w') as arquivo1:
        json.dump(user, arquivo1)