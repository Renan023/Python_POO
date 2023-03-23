from Pessoa import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
import time
class Estudante(Pessoa):
    def __init__(self,nome,rg,cpf,phone,email,nasc,idade,sexo, aluno,av=0):
        super().__init__(nome,rg,cpf,phone,email,nasc,idade, sexo)
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
        return f'{self.nome} ,{self.rg},{self.cpf},{self.phone},{self.email},' \
               f'  {self.nasc} , {str(self.idade)},{self.sexo} , {self.aluno} , {self.av:.2f}'
    
    def write(self,jan, nome):
        try:
            a = open(jan,'at')
        except:
            print(f'Erro no cadastro ')

        else:
            a.write(f'{nome}\n')


    def send_mail(self,assunto, de, para):
        body = f"Aluno {self.nome}\n" \
               f"{self.nome},RG {self.rg} e CPF {self.cpf} nascido no ano {self.nasc}, cuja idade no ano corrente" \
               f"é de {self.idade} anos, sua média é de {self.av}"
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

        texto = f'{self.nome} foi confirmado que é aluno e sua {self.av}. Consulte o email para informações' \
                f' mais detalhadas'
        link = f"https://web.whatsapp.com/send?phone={self.phone}&text={texto}"
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get('https://web.whatsapp.com')
        time.sleep(20)
        browser.get(link)
        time.sleep(20)