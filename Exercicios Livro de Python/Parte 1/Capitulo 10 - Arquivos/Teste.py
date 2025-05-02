
caminho = 'C:/Users/EPIC!-PC/Documents/GitHub/Python-intensivo/Exercicios Livro de Python/Parte 1/Capitulo 10 - Arquivos/Importações/Pi.txt'


with open(caminho) as arquivo:
    conteudo = arquivo.read()
    print(conteudo.rstrip())