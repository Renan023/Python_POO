from Pessoa import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class Professor(Pessoa):

    def __init__(self,nome,rg,cpf,phone,email,nasc,idade ,sexo ,salario, materia,tempo,carga,exp,desc,plus,novo,atual):
        super().__init__(nome,rg,cpf,phone,email,nasc,idade ,sexo)
        self.materia = materia
        self.salario = salario
        self.tempo = tempo  # quantas horas de trabalho
        self.carga = carga  # horas semanais
        self.exp = exp  # tempo de experiência
        self.desc = desc  # desconto
        self.plus = plus  # aumento
        self.novo = self.salario * plus / 100 + self.salario  # novo salário
        self.atual = self.novo * (-desc) / 100 + self.novo  # salário final



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


    def write(self,jan, nome):
        try:
            a = open(jan,'at')
        except:
            print(f'Erro no cadastro')
        else:
            a.write(f'{nome}')


    def __str__(self):
        super(Professor, self).__str__()
        return f'{self.nome} ,{self.rg},{self.cpf},{self.phone},{self.email}, ' \
               f'{self.nasc} , {str(self.idade)},  {self.sexo} , {self.materia} , ' \
               f'{self.salario} , {self.tempo} , {self.carga} , {self.exp} , {self.desc} , {self.plus} ,' \
               f'{self.novo} ,  {self.atual}'


    def send_mail(self,assunto, de, para):
        body = f"Professor {self.nome}\n" \
               f"{self.nome} portador do RG {self.rg} e CPF {self.cpf}, nascido no ano {self.nasc} com idade no " \
               f"ano corrente {self.idade} anos, de sexo {self.sexo} leciona matéria {self.materia} seu salário base é de R$" \
               f"{self.salario} seu salário stual com descontos ou acréscimos é de R$ {self.atual}"
        msg = MIMEMultipart()
        msg['Subject'] =  "" + assunto
        msg['From'] = "" + de
        msg['To'] = "" + para
        password = "hyxzgercfczyggxz"
        msg.attach(MIMEText(body,'plain'))

        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.starttls()
        server.login(msg['From'],password)
        server.sendmail(msg['From'],msg['To'],msg.as_string())
        server.quit()