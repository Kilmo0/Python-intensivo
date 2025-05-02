class restaurante():
    """digite o nome do restaurante, e o tipo de culinária"""

    def __init__(self, nome, culinaria):
        self.nome = nome
        self.culinaria = culinaria
        self.servidos = 0
    
    def descrever(self):
        print(f'o restaurante se chama: {self.nome}')
        print(f'o restaurante possue a gastronomia: {self.culinaria}')
        print(f'O restaurante já atendeu {self.servidos} clientes')

    def serviço(self, valor):
        self.servidos = self.servidos + valor



class sorveteria(restaurante):
    def __init__(self, nome, culinaria, *sabores):
        super().__init__(nome, culinaria, )
        self.sabores = sabores
    
    def sabores_sorvete(self):
       print('os sabores de chocolate de nossa sorveteria são:\n')
       for sabor in self.sabores:
           print(sabor)

camin = sorveteria('sorvete', 'sorvetes', 'Morango', 'chocolate', 'creme')
camin.sabores_sorvete()