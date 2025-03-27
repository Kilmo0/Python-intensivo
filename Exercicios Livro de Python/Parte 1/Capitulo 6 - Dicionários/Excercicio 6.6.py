favlinguagem = {
    'Kauã': 'java',
    'Allan': 'php',
    'Brian': 'Rust',
    'Brian': 'Assembly',
    'Gabriel': 'C++', 
    'Amanda': 'java'
}

particiobrigado = ['Brian', 'Kauã', 'Gabriel', 'Amanda', 'Julio']

for participante in particiobrigado:
    if participante not in favlinguagem.keys():
        print(f'por favor {participante}, responda o questionário')
    else:
        print(f'obrigado por participar do questionário {participante}')
