respostas = {}

questionario = True

while questionario:
    nome = input('por favor digite seu nome')
    resposta = input('qual montamnha você gostaria de escolar?')
    respostas[nome] = resposta    
    repetir = input('você gostaria de que outra pessoa respondesse?')
    if repetir == 'não':
        questionario = False
print('-'*5 + 'Resultado' + '-'*5)
for nome, resposta in respostas.items():
    print(respostas)
