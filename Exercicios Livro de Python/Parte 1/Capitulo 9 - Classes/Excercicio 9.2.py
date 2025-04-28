class restaurante():
    """digite o nome do restaurante, e o tipo de culinária"""

    def __init__(self, nome, culinaria):
        self.nome = nome
        self.culinaria = culinaria

    def descrever(self):
        print(f'o restaurante se chama: {self.nome}')
        print(f'o restaurante possue a gastronomia: {self.culinaria}')
    

amandares = restaurante('Lá Nuuty', 'restaurante de massas')
kauares = restaurante('Spaciba', 'restaurante de comunidas do leste europeu')
samuelres = restaurante('Kartoffelklösse', 'restaurante germinico')

amandares.descrever()
kauares.descrever()
samuelres.descrever()