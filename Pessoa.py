import char,datetime
at = datetime.datetime.today().year

class Pessoa:
    def __init__(self,nome,nasc,sexo):
        self.nome = nome
        self.nasc = nasc
        self.sexo = sexo


    def dados(self):
        char.principal('Confirmação')
        print(f'Nome {self.nome}')
        print(f'Nascimento {self.nasc}')
        self.idade = at- self.nasc
        print(f'Idade {self.idade} anos')
        if self.idade >=18:
            print(f'{self.nome} é de maior')
        else:
            m= 18 - self.idade
            print(f'Falta {m} anos para {self.nome} chegar a maioridade')
        if self.sexo not in 'Ff':
            print('Sexo Masculino')
        else:
            print('Sexo Feminino')