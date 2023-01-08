import char,datetime
import re

at = datetime.datetime.today().year

class Pessoa:
    def __init__(self,nome,nasc,idade ,sexo):
        self.nome = nome
        self.nasc = nasc
        self.idade = at - nasc
        self.sexo = sexo


    def __str__(self):
        return f'{self.nome} , {self.nasc} ,{self.idade},{self.sexo}'

    def dados(self):
        char.principal('Confirmação')
        print(f'Nome {self.nome}')
        print(f'Nascimento {self.nasc}')
        self.idade = at- self.nasc
        print(f'Idade {self.idade} anos')
        if self.idade >=18:
            pass
        else:
            m= 18 - self.idade
            print(f'Falta {m} anos para chegar a maioridade')
        if self.sexo not in 'Ff':
            print('Sexo Masculino')
        else:
            print('Sexo Feminino')

    def write(self,jan, nome):
        try:
            a = open(jan, 'at')
        except:
            print(f'Erro no cadastro ')

        else:
            a.write(f'{nome}\n ')
