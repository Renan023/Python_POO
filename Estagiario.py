import Pessoa

class Estagiario(Pessoa.Pessoa):

    def __init__(self,nome,nasc,idade,sexo,tempo,horas,carga):
        super(Estagiario, self).__init__(nome,nasc,idade,sexo)
        self.tempo = tempo#tempo de contrato
        self.horas = horas # horas de trabalho por dia
        self.carga = carga # horas semanal


    def dados(self):
        super(Estagiario, self).dados()