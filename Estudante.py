import Pessoa


class Estudante(Pessoa.Pessoa):
    def __init__(self,nome,nasc,idade,sexo, aluno,av=0):
        super().__init__(nome,nasc,idade, sexo)
        self.aluno = aluno#aluno ou não - verdadeiro ou falso
        self.av = av#quantas avaliações e média


    def dados(self):
        super(Estudante, self).dados()
        if self.aluno not in 'Nn':
            print(f'{self.nome} é aluno')
            if self.av >= 6 and self. aluno not in 'Nn':
                print(f'{self.nome} foi aprovado com nota {self.av}')
            elif self.av >= 4 and self.av < 6 and self.aluno == True:
                rec = 10 - self.av
                print(f'{self.nome} está de recuperação e precisa tirar {rec} para passar')
            else:
                print(f'{self.nome} foi reprovado sua média {self.av}')
        else:
            print(f'{self.nome} sua nota é de {self.av}')

