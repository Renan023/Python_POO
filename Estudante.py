import Pessoa


class Estudante(Pessoa.Pessoa):
    def __init__(self,nome,nasc,sexo,aluno,av=0):
        super().__init__(nome,nasc,sexo)
        self.aluno = aluno
        self.av = av


    def dados(self):
        super(Estudante, self).dados()
        if self.aluno == True:
            print(f'{self.nome} é aluno')
            if self.av >= 6 and self. aluno == True:
                print(f'{self.nome} foi aprovado com nota {self.av}')
            elif self.av >= 4 and self.av < 6 and self.aluno == True:
                rec = 10 - self.av
                print(f'{self.nome} está de recuperação e precisa tirar {rec} para passar')
            else:
                print(f'{self.nome} foi reprovado sua média {self.av}')
        else:
            print(f'{self.nome} ainda não é aluno ')
        print(f'{self.nome} sua nota é de {self.av}')

