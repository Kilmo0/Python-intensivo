def newuser(nome, sobrenome, **info):
    user = {}
    user['nome'] = nome
    user['sobrenome'] = sobrenome
    for chave, valor in info.items():
        user[chave] = valor
    return user

user01 = newuser('Kauã', 'Lorenzi', profissão='Engenheiro de software')
print(user01)