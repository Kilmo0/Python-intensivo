print('Prazer, Por favor informe sua idade para saber o valor')
active = True

idade = ''
while active:
    idade = input()
    if idade <= 3:
        print('Seu ingreço é free')
    elif idade <= 12:
        print('Seu ingreço é 10 doletas')
    elif idade >= 13:
        print('Seu ingreço é 15 doletas')
    else:
        active = False