def modelos_impressos(modnaoimpresso, modcompleto):
    while modnaoimpresso:
        sendofeito = modnaoimpresso.pop()
        print(f'Imprimindo {sendofeito}')
        modcompleto.append(sendofeito)

def modelos_completos(modeloscompleto):
    print('\nOs modelos completos foram:')
    for feito in modeloscompleto:
        print(feito)

modeloshaserfeito = ['Marios Bros', 'IphoneCase', 'Capacitor']
modeloscompletos = []

modelos_impressos(modeloshaserfeito, modeloscompletos)
modelos_completos(modeloscompletos)