from Pessoa import *



class Estudante(Pessoa):
    def __init__(self,nome,nasc,idade,sexo, aluno,av=0):
        super().__init__(nome,nasc,idade, sexo)
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


    def __str__(self):
        super(Estudante, self).__str__()
        return f'{self.nome} ,  {self.nasc} , {str(self.idade)},' \
               f'{self.sexo} , {self.aluno} , {self.av:.2f}'
    
    def write(self,jan, nome):
        try:
            a = open(jan,'at')
        except:
            print(f'Erro no cadastro ')

        else:
            a.write(f'Dados -> {nome}\n')