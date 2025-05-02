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




