import numeros

def principal(msg):
    print('='*100)
    print(msg.center(100))
    print('='*100)

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
            sexo = char(sexo).strip().upper()[0]
            while sexo not in 'MmFf':
                print('\033[31mDigite um valor aceito\033[m ')
                sexo = char('Sexo[M/F] ').strip().upper()[0]
        except(KeyboardInterrupt):
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return sexo


def opção(op):

    while True:
        try:
            op = numeros.inteiro(op)
            while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
                print(f'\033[31mOpção inválida\033[m')
                op = numeros.inteiro('Estudante[1]/Estagiário[2]/Funcionário[3]/Professor[4]/Visitante[5] ')
        except (KeyboardInterrupt):
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return op


def aluno(aluno):

    while True:
        try:
            aluno = char(aluno).strip().upper()[0]
            while aluno not in 'SsNn' and aluno != '':
                print(f'\033[31mDigite uma informação válida\033[m')
                aluno = char('Aluno[S/N] ').strip().upper()[0]
        except (KeyboardInterrupt):
            print(f'\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return aluno

def periodo(periodo):

    while True:
        try:
            periodo = char(periodo).strip().upper()[0]
            while periodo not in 'MmTtNn':
                print('\033[31mDigite novamente uma informação válida\033[m')
                periodo = char('Período[M/T/N] ').strip().upper()[0]
        except (KeyboardInterrupt):
            print('033[31mInterrompkido pelo  usuário\033[m')
            break
        else:
            return periodo