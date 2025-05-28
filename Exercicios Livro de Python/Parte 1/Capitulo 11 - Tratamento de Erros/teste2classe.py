import unittest
from Importações.importest import comprimento as comando

class nomesdeteste(unittest.TestCase):
    """Testa o nome"""
    
    def testdenome(self):
        """Nome Funciona?"""
        nomeformatado = comando('Kauã', 'Lorenzi')
        self.assertEqual(nomeformatado, 'olá Kauã Lorenzi como você está?')

unittest.main()