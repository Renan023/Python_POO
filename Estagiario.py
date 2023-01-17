from Pessoa import *

class Estagiario(Pessoa):

    def __init__(self,nome,nasc,idade,sexo,tempo,horas,carga,periodo,b_aux,noturno):
        super().__init__(nome,nasc,idade,sexo)
        self.tempo = tempo#tempo de contrato
        self.horas = horas # horas de trabalho por dia
        self.carga = carga # horas semanal
        self.periodo = periodo#periodo
        self.b_aux = b_aux #bolsa auxilio
        self.noturno = self.b_aux * 115 /100


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


    def write(self,jan, nome):
        try:
            a = open(jan,'at')
        except:
            print(f'Erro no cadastro')
        else:
            a.write(f'Dados -> {nome}')


    def __str__(self):
        super(Estagiario, self).__str__()
        return f'{self.nome} , {self.nasc} , {str(self.idade)}, {self.sexo} , {self.tempo} , {self.horas} , ' \
               f'{self.carga} , {self.periodo} , {self.b_aux} , {self.noturno}'


