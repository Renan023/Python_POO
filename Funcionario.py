import Pessoa

class Funcionario(Pessoa.Pessoa):

    def __init__(self,nome,nasc,idade,sexo,funcao,salario,tempo,carga,exp,desc,plus,novo,atual ):
        super(Funcionario, self).__init__(nome,nasc,idade,sexo)
        self.funcao = funcao
        self.salario =salario
        self.tempo = tempo # quantas horas de trabalho
        self.carga = carga # horas semanais
        self.exp = exp# tempo de experiência
        self.desc = desc#desconto
        self.plus = plus#aumento
        self.novo = self.salario*plus/100+self.salario#novo salário
        self.atual = self.novo*desc/100+self.novo#salário final


    def dados(self):
        super(Funcionario, self).dados()
        if self.tempo >10:
            bon = self.tempo * 110 / 100
            print(f'{self.nome} tem uma bonificação de 10% no salário este mês irá receber R$ {bon:.2f}')
        else:
            print(f'Não houve nenhbuma bonificação seu salário ficou em R$ {self.salario:.2f}')
        if self.carga >=45 and self.exp >= 5 :
            plus = self.salario *145/100
            print(f'{self.nome} por seu desempenho seu salário irá receber um aumento fixo de R$ {plus:.2f}')
        else:
            print(f'{self.nome}, infelizmente não foi cumprido os pré requisitos. Não desista ')