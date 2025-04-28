import time

def imprimir_modelos(listademodelos, modeloscompleto=[]):
    while listademodelos:
        print('modelos na memoria:')
        print('-'*25)
        for imprimindo in listademodelos:
            print(imprimindo.title())
        print('')
        time.sleep(5)
        print('-'*5 + 'imprimindo', '-'*5)
        imprimindomodelo = listademodelos.pop()
        print(f'imprimindo o modelo: {imprimindomodelo}\n')
        modeloscompleto.append(imprimindomodelo)
        time.sleep(5)
        print('-'*5 + 'Modelos Finalizados' + '-'*5)
        print(f'modelos finalizado: {modeloscompleto}\n')
        time.sleep(3)
        print('-'*20 + '\n'*3)
        time.sleep(3)
    

