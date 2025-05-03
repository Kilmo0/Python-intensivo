active = True
filename = 'Book.txt'


with open(filename, 'w', encoding='UTF-8') as arquivo:
    while active:
        print('digite 1 para finalizar')
        questionario = input('porque você gosta programar?')
        if questionario == '1':
            break
        else:
            arquivo.write(questionario + '\n')