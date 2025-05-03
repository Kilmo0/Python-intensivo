print('escolha um número para dividir 5')
num1 = int (input())
try:
    print(5 / num1)
except ZeroDivisionError:
    print('tu é burro para caralho para dividir algo por 0')
