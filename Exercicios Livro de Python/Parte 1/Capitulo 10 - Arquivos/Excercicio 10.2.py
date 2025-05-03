with open('C:/Users/EPIC!-PC/Documents/GitHub/Python-intensivo/Exercicios Livro de Python/Parte 1/Capitulo 10 - Arquivos/importar/Aprendendo.txt', encoding='UTF-8') as arquivo:
    aprendizado = arquivo.read()

aprendizado = aprendizado.replace('listas', 'Tuplas')
print(aprendizado)