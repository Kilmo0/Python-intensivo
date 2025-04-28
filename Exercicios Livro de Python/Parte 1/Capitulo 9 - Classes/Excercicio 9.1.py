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

amandares = restaurante('Lá Nuuty', 'restaurante de massas')
amandares.serviço(30)
amandares.descrever()