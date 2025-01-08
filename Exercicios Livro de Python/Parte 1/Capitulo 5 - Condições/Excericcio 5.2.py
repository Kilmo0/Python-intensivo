"""
5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que
criar em dez. Se quiser testar mais comparações, escreva outros testes e acrescente-
os em conditional_tests.py. Tenha pelo menos um resultado True e um False para
cada um dos casos a seguir:
• testes de igualdade e de não igualdade com strings;
• testes usando a função lower();
• testes numéricos que envolvam igualdade e não igualdade, maior e menor que,
maior ou igual a e menor ou igual a;
• testes usando as palavras reservadas and e or;
• testes para verificar se um item está em uma lista;
• testes para verificar se um item não está em uma lista
"""

#teste de string e lower
texto = 'Alfabeto'
print(texto == 'Alfabeto')
print(texto.lower() == 'Alfabeto')

print('-'*20)

#teste numerico simples
numero = 7
print(numero >= 8)
print(numero <= 5)
print (numero > 6)
print('-'*20)

#argumentação númerica complexa
numero2 = 13
if numero or numero2 >= 9:
    print(True)

print(numero == 7 and numero2 == 13)
print('-'*20)

#argumentação em lista
comprar = ['tomada', 'dijuntor', 'fio', 'capacitor']
print('Baterias' in comprar)
print('fio' in comprar) 