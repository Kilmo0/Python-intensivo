import unittest
from Importações.midname import nomedomeio

class Testenomedomeio(unittest.TestCase):
    """testar variavel"""
    
    def teste_nome_meio(self):
        resultado = nomedomeio('kaua','Lorenzi', 'Mantai')
        self.assertEqual(resultado, 'kaua Mantai Lorenzi')

unittest.main()