import Pessoa
import arquivos


class Estudante(Pessoa.Pessoa):
    def __init__(self,cat,nome,nasc,idade,sexo, aluno,av=0):
        super().__init__(cat,nome,nasc,idade, sexo)
        self.aluno = aluno#aluno ou não - verdadeiro ou falso
        self.av = av#quantas avaliações e média


    def dados(self):
        super(Estudante, self).dados()
        if self.aluno not in 'Nn':
            print(f'É aluno')
            if self.av >= 6 and self. aluno not in 'Nn':
                print(f'Foi aprovado com nota {self.av}')
            elif self.av >= 4 and self.av < 6 and self.aluno == True:
                rec = 10 - self.av
                print(f'Está de recuperação e precisa tirar {rec} para passar')
            else:
                print(f'Foi reprovado sua média {self.av}')
        else:
            print(f'Sua nota é de {self.av}')


