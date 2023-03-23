import char,datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
import time

at = datetime.datetime.today().year
remetente = ''
class Pessoa:
    def __init__(self,nome,rg,cpf,phone,email,nasc,idade ,sexo):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.phone = phone
        self.email = email
        self.nasc = nasc
        self.idade = at - nasc
        self.sexo = sexo


    def __str__(self):
        return f'{self.nome} ,{self.rg},{self.cpf},{self.phone},{self.email}, {self.nasc} ,{str(self.idade)},{self.sexo}'

    def dados(self):
        char.principal('Confirmação')
        print(f'Nome {self.nome}')
        print(f'RG {self.rg}')
        print(f'CPF {self.cpf} ')
        print(f'Telefone/WPP {self.phone}')
        print(f'E-mail {self.email}')
        print(f'Nascimento {self.nasc}')
        self.idade = at- self.nasc
        print(f'Idade {self.idade} anos')
        if self.idade >=18:
            pass
        else:
            m= 18 - self.idade
            print(f'Falta {m} anos para chegar a maioridade')
        if self.sexo not in 'Ff':
            print('Sexo Masculino')
        else:
            print('Sexo Feminino')

    def write(self, jan, nome):
        try:
            a = open(jan, 'at')
        except:
            print(f'Erro no cadastro')
        else:
            a.write(f'{nome}')
    def send_mail(self,assunto, de, para):
        body = f"Cadastro de {self.nome}\n" \
               f"{self.nome} fez o cadastro de visitante, no qual o RG {self.rg} e CPF {self.cpf}" \
               f"seu ano de nascimento é {self.nasc} com idade {self.idade} anos, no ano corrente e sexo {self.sexo}"
        msg = MIMEMultipart()
        msg['Subject'] = "" + assunto
        msg['From'] = "" + de
        msg['To'] = "" + para
        password = ""
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

    def wpp(self):

        texto = f'Olá {self.nome}, você terminou seu cadastro e seja muito bem vindo, você receberá também um e-mail confirmando o cadastro. Obrigado =]'
        link = f"https://web.whatsapp.com/send?phone={self.phone}&text={texto}"
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get('https://web.whatsapp.com')
        time.sleep(20)
        browser.get(link)
        time.sleep(20)