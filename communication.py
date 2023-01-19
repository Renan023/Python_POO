from char import *

def phone(phone):

    phone = char(phone)
    if len(phone) == 13:
        print(f'\033[34mTelefone/Wpp aceito\033[m')
    while len(phone) != 13:
        print('\033[31mTelefone/Wpp inválido\033[m')
        phone = char('Telefone/Wpp ')
        print(f'\033[34mTelefone/Wpp aceito\033[m')


def email(email):

    email = char(email)
    cemail = char('Confirme o email informado ')
    if email == cemail:
        print(f'\033[34mEmail confirmado com sucesso\033[m')
    else:
        while email not in cemail:
            print(f'\033[31mEmail informado diferente informe o email novamente\033[m')
            email = char('Email ')
            cemail = char('Confirme o email informado ')
            if email == cemail:
                print(f'\033[34mEmail confirmado com sucesso\033[m')


email('Email ')