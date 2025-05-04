while True:
    try:
        num1 = input('digite o primeiro numero')
        num2 = input('digite o segunda numero')
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print(f'{num1} ou {num2} não são números')
        break
    else:
        total = num2 + num1
        print(f'A soma de {num1} e {num2} é: {total}')

