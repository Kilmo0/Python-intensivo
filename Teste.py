respostas = {}


questionario = True

while questionario:
    nome = input('qual o seu nome?\n')
    resposta = input('Qual montanha você gostaria de escalar algum dia?\n')
    respostas[nome] = resposta
    repetir = input('você gostaria que outra pessoa respondesse?')
    if repetir == 'não':
        questionario = False
print('-'*5 + 'Resuldado' + '-'*5)
for nome, resposta in respostas.items():
    print(respostas)