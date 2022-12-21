import Pessoa


class Professor(Pessoa.Pessoa):

    def __init__(self,cat,nome,nasc,idade ,sexo ,salario, materia,tempo,carga,exp,desc,plus,novo,atual):
        super().__init__(cat,nome,nasc,idade ,sexo)
        self.materia = materia
        self.salario = salario
        self.tempo = tempo  # quantas horas de trabalho
        self.carga = carga  # horas semanais
        self.exp = exp  # tempo de experiência
        self.desc = desc  # desconto
        self.plus = plus  # aumento
        self.novo = self.salario * plus / 100 + self.salario  # novo salário
        self.atual = self.novo * desc / 100 + self.novo  # salário final



    def dados(self):
        super(Professor, self).dados()
        print(f'Matéria {self.materia}')
        print(f'Salário base R$ {self.salario:.2f}')
        print(f'Horas de trabalho diárias {self.tempo:.0f} hrs')
        print(f'Horas semanais {self.carga:.0f} hrs')
        print(f'Tempo de trabalho {self.exp:.0f} ano(s)')
        print(f'Desconto no salário {self.desc} %')
        print(f'Acréscimo no {self.plus} %')
        if self.tempo > 10:
            bon = self.tempo * 110 / 100
            print(f'Bonificação de 10% no salário este mês irá receber R$ {bon:.2f}')
        else:
            print(f'Não houve nenhuma bonificação seu salário ficou em R$ {self.salario:.2f}')
        if self.carga >= 45 and self.exp >= 5:
            plus = self.salario * 145 / 100
            print(f'Seu salário irá receber um aumento fixo de R$ {plus:.2f}')
        else:
            print(f'O salário ficou em R$ {self.atual}')
            print(f'Infelizmente não foi cumprido os pré requisitos. Não desista ')
