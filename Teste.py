from collections import OrderedDict

favlinguagem = OrderedDict()

favlinguagem['Amanda'] = 'Java'
favlinguagem['Brian'] = 'Assembly'
favlinguagem['João'] = 'Python'
favlinguagem['Rosana'] = 'Php'

for chave, valor in favlinguagem.items():
    print(chave, valor)