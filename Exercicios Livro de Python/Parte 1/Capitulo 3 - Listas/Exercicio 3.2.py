"""
3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas. O
texto de cada mensagem deve ser o mesmo, porém cada mensagem deve estar
personalizada com o nome da pessoa.
"""

names = ['brian', 'allan', 'gabriel', 'Anton', 'Alexandre']

for name in names:
    print('olá {} tudo bem com você?'.format(name))
