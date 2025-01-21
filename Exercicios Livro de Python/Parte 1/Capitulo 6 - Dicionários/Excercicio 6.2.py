"""
6.2 – Números favoritos: Use um dicionário para armazenar os números favoritos
de  algumas  pessoas.  Pense  em  cinco  nomes  e  use-os  como  chaves  em  seu
dicionário. Pense em um número favorito para cada pessoa e armazene cada um
como um valor em seu dicionário. Exiba o nome de cada pessoa e seu número
favorito. Para que seja mais divertido ainda, faça uma enquete com alguns amigos
e obtenha alguns dados reais para o seu programa
"""

Usuários = [
    {'Nome':'Kauã Lorenzi', 'Numero': '1'},
    {'Nome':'Izaque Samuel', 'Numero': '4'},
    {'Nome':'Layon Ruan', 'Numero': '22'},
    {'Nome':'Amanda Janke', 'Numero': '99'},
    {'Nome':'Allan', 'Numero': '14'}
] 

for usuario in Usuários:
    print('a pessoa {} gosta do numero {}!'.format(usuario['Nome'], usuario['Numero']))