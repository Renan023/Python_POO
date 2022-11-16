import numeros

def principal(msg):
    print('='*50)
    print(msg.center(50))
    print('='*50)

def char(ch):
    while True:
        try:
            ch = input(ch)
        except (KeyboardInterrupt):
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return ch

def sexo(sexo):

    while True:
        try:
            sexo = char(sexo).strip().upper()
            while sexo not in 'MmFf':
                print('\033[31mDigite um valor aceito\033[m ')
                sexo = char('Sexo[M/F] ').strip().upper()[0]
        except (ValueError, TypeError):
            print('\033[31mDigite um valor aceito\033[m ')
            sexo = char('Sexo[M/F] ').strip().upper()[0]
        except(KeyboardInterrupt):
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return sexo


def opção():

    while True:
        try:
            op = numeros.inteiro('Estudante[1]/Estagiário[2]/Funcionário[3]/Professor[4]/Visitante[5] ')
            while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
                print(f'\033[31mOpção inválida\033[m')
                op = numeros.inteiro('Estudante[1]/Estagiário[2]/Funcionário[3]/Professor[4]/Visitante[5] ')
        except (KeyboardInterrupt):
            print('\033[31mInterrompido pelo teclado\033[m')
            break
        else:
            return op