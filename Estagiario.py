import Pessoa

class Estagiario(Pessoa.Pessoa):

    def __init__(self,cat,nome,nasc,idade,sexo,tempo,horas,carga,periodo,b_aux,noturno):
        super().__init__(cat,nome,nasc,idade,sexo)
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


    def write(self,jan, categoria):
        try:
            a = open(jan,'at')
        except:
            print(f'Erro no cadastro')
        else:
            a.write(f'Dados -> {categoria}')


    def __str__(self):
        super(Estagiario, self).__str__()
        return f'Categoria {self.categoria} , Nome {self.nome} , Nasc {self.nasc} , Idade {self.idade},' \
               f'Sexo {self.sexo} , Contrato {self.tempo} , Horas diárias {self.horas} , Hora semanal {self.carga} , ' \
               f'Período {self.periodo} , Bolsa auxilio {self.aux} , Bolsa Auxilio Total {self.noturno}'


