import time
from selenium import webdriver
from char import *


def phone(phone):
    while True:
        try:
            phone = char(phone)
            if len(phone) == 15:
                print(f'\033[31mDigite um telefone válido\033[m')
                while len(phone) != 15:
                    print('\033[31mTelefone/Wpp inválido\033[m')
                    phone = char('Telefone/Wpp ')
        except(KeyboardInterrupt):
            print(f'\033[31mInterrompido pelo usuário\033[m')
        else:
            return phone


def email(email):
    while True:
        try:
            email = char(email)
            cemail = char('Confirme o email informado ')

            while email not in cemail:
                print(f'\033[31mEmail informado diferente informe o email novamente\033[m')
                email = char('Email ')
                cemail = char('Confirme o email informado ')
                if email == cemail:
                    print(f'\033[34mEmail confirmado com sucesso\033[m')
        except (KeyboardInterrupt):
            print(f'\033[31mInterrompido pelo usuário\033[m')
        else:
            return email

def agradecimento():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get('file:///C:/Users/user/Downloads/IMAGEM-DO-AWEBIC-11-1-1536x806.webp')
    time.sleep(20)

