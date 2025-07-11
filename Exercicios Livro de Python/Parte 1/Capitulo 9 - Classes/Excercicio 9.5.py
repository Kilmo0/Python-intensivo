class user():
    def __init__(self, nome, sobrenome, idade, corfav):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.corfav = corfav
        self.tentativas_login = 1
        self.bloqueado = False

    def descrição(self):
        """função que descreve o usuario"""
        if self.bloqueado:
            print('você foi bloqueado, contate um administrador')
            return
        print(f'nome: {self.nome.title()} {self.sobrenome.title()}')
        print(f'idade: {self.idade} anos')
        print(f'cor favorita: {self.corfav}')

    def resetar_tentativas(self):
        self.tentativas_login = 0
        self.bloqueado = False

    def acrecentar_tentativas(self, vezes):
        if self.bloqueado:
            print('você foi bloqueado, contate um administrador')
            return
        self.tentativas_login = vezes
        if self.tentativas_login >= 10:
            print('você foi bloqueado, entre em contato com o administrador')
            self.bloqueado = True
        else:
            print(f'numeros de tentativas: {self.tentativas_login}')
        

user01 = user('Kauã', 'Lorenzi', 19, 'Roxo')

user01.acrecentar_tentativas(15)
#user01.descrição()

user01.descrição()
user01.resetar_tentativas()
user01.descrição()




