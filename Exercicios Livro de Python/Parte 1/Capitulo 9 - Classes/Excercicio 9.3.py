class user():
    def __init__(self, nome, sobrenome, idade, corfav):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.corfav = corfav

    def descrição(self):
        """função que descreve o usuario"""
        print(f'nome: {self.nome.title()} {self.sobrenome.title()}')
        print(f'idade: {self.idade} anos')
        print(f'cor favorita: {self.corfav}')

user01 = user('Kauã', 'Lorenzi', 19, 'Roxo')

user01.descrição()




