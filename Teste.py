def nomecompleto(nome, sobrenome):
    nomecompletado = nome + ' ' + sobrenome
    return nomecompletado

#questionario = True

while True:
    print('digite "q", para sair')
    nome = input('digite seu primeiro nome: ')
    if nome == 'q':
        break
    sobrenome = input('digite seu sobrenome ')
    if sobrenome == 'q':
        break
    asd = nomecompleto(nome, sobrenome)
    print(asd.title())