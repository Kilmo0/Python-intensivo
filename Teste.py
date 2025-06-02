class carro():
    """Cria a descrição de um carro"""
    def __init__(self, nome, modelo, ano):
        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.quilometros = 0

    def descrever(self):
        """Descreve o carro"""
        print('-'*30)
        descrevercarro = f'Nome: {self.nome}\nModelo: {self.modelo}\nAno: {self.ano}'
        return descrevercarro
    
    def quilometragem(self):
        """Descreve a quilometragem do carro"""
        print(f'seu carro tem {self.quilometros}km')

    def updatequilimetros(self, valor):
        """Atualiza a quilimetragem"""
        self.quilometros = valor

meucarro = carro('Tucson', 'G44', '2015')
print(meucarro.descrever())
meucarro.updatequilimetros(100)
meucarro.quilometragem()