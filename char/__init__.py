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
                sexo = char('Sexo[M/F] ').strip().upper()
        except (ValueError, TypeError):
            print('\033[31mDigite um valor aceito\033[m ')
            sexo = char('Sexo[M/F] ').strip().upper()
            continue
        except(KeyboardInterrupt):
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return sexo