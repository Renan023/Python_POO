import Pessoa

class Estagiario(Pessoa.Pessoa):

    def __init__(self,nome,nasc,idade,sexo,tempo,horas,carga,periodo,b_aux):
        super(Estagiario, self).__init__(nome,nasc,idade,sexo)
        self.tempo = tempo#tempo de contrato
        self.horas = horas # horas de trabalho por dia
        self.carga = carga # horas semanal
        self.periodo = periodo#periodo
        self.b_aux = b_aux #bolsa auxilio


    def dados(self):
        super(Estagiario, self).dados()
        print(f'Contrato de {self.tempo} ano(s)')
        print(f'Horas de trabalho por dia {self.horas} hrs')
        print(f'Horas semanais {self.carga} hrs')
        if self.periodo in 'Mm':
            print(f'Período Matutino')
            print(f'Bolsa auxilio R$ {self.b_aux:.2f}')
        elif self.periodo in 'Tt':
            av = self.b_aux *105/100
            print('Período Vespertino')
            print(f'Bolsa auxilio R$ {self.b_aux:.2f} com adicional de 5% R$ {av:.2f}')
        elif self.periodo in 'Nn':
            plus = self.b_aux * 115 /100
            print('Período Noturno')
            print(f'Bolsa auxilio R$ {self.b_aux:.2f} com adicional de 15% R$ {plus:.2f}')