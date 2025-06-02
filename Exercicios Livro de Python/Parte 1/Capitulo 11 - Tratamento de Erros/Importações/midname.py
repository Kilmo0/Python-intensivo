def nomedomeio(nome, sobrenome, meio=''):
    if meio:
        nomecommeio = f'{nome} {meio} {sobrenome}'
    else:
        nomecommeio = f'{nome} {sobrenome}'
    return nomecommeio
