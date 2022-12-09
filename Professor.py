import Funcionario


class Professor(Funcionario.Funcionario):

    def __init__(self,nome,nasc,idade,sexo,funcao,salario,tempo,carga,exp,desc,plus,novo,atual, materia):
        super(Professor, self).__init__(self,nome,nasc,idade,sexo,funcao,salario,tempo,carga,exp,desc,plus,novo,atual )
        self.materia = materia



    def dados(self):
        super(Professor, self).dados()
        print(f'Matéria {self.materia}')