from Pessoa import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
from selenium import webdriver

class Estagiario(Pessoa):

    def __init__(self,nome,rg,cpf,phone,email,nasc,idade,sexo,tempo,horas,carga,periodo,b_aux,noturno):
        super().__init__(nome,rg,cpf,phone,email,nasc,idade,sexo)
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
            a.write(f'{nome}')


    def __str__(self):
        super(Estagiario, self).__str__()
        return f'{self.nome} ,{self.rg},{self.cpf},{self.phone},{self.email}, ' \
               f'{self.nasc} , {str(self.idade)}, {self.sexo} , {self.tempo} , {self.horas} , ' \
               f'{self.carga} , {self.periodo} , {self.b_aux} , {self.noturno}'


    def send_mail(self,assunto, de, para):
        body = f"Estagiário {self.nome}\n" \
               f"{self.nome} portador do RG {self.rg} e CPF {self.cpf} nascido no ano de {self.nasc} com idade no " \
               f"ano corrente de {self.idade} anos, no sexo {self.sexo}, estagiando com o contrato de {self.tempo} ano(s)" \
               f" no período {self.periodo}, recebendo uma bolsa auxilio de R$ {self.noturno}"
        msg = MIMEMultipart()
        msg['Subject'] = "" + assunto
        msg['From'] = "" + de
        msg['To'] = "" + para
        password = ""
        msg.attach(MIMEText(body,'plain'))

        server = smtplib.SMTP('smtp.gmail.com',port=587)
        server.starttls()
        server.login(msg['From'],password)
        server.sendmail(msg['From'],msg['To'],msg.as_string())
        server.quit()


    def wpp(self):

        texto = f'{self.nome} sua bolsa auxilio total de estagiário é {self.noturno}. Consulte o email para informações ' \
                f'mais detalhadas'
        link = f"https://web.whatsapp.com/send?phone={self.phone}&text={texto}"
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get('https://web.whatsapp.com')
        time.sleep(20)
        browser.get(link)
        time.sleep(40)
