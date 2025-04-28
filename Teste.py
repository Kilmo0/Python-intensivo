class car():
    """inicia os atributos que fazem a descrição do carro"""
    def __init__(self, nome, modelo, ano):
        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = 30
        self.gas = '8L'

    def descrever(self):
        """descreve o nome completo do carro"""
        nomecompleto = f'{self.nome} modelo {self.modelo} ano {self.ano}'
        return nomecompleto

    def quilometros(self):
        print(f'esse carro tem {self.quilometragem}KM')   

    def updatequilimetragem(self, valor):
        if valor >= self.quilometragem:
            self.quilometragem = valor
        else:
            print('você não pode diminuir quilometragem')

    def adicionarquilometragem(self, valor):
        self.quilometragem = self.quilometragem + valor

    def gasolina(self):
        print(f'o carro tem {self.gas} de gasolina')


class bateria():
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

meutesla = carro_eletrico('Tesla', 'G4', '2016')

meutesla.bateria.descrever_bateria()