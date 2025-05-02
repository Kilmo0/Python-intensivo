from Car import car

class bateria(car):
    def __init__(self, bateria_carro=70):
        self.bateria_carro = bateria_carro

    def descrever_bateria(self):
        print(f'esse carro possue uma bateria de {self.bateria_carro}KWh')

class carro_eletrico(car):

    def __init__(self, nome, modelo, ano):
        super().__init__(nome, modelo, ano)
        self.bateria = bateria()

    def gasolina(self):
        print('carros eletricos não tem gasolina')
