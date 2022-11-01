def inteiro(n):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mDigite um número válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return n

def real(f):
    while True:
        try:
            f=float(input(f))
        except (ValueError, TypeError):
            print('\033[31mDigite um valor aceito\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return f


def av(notas):
    xs = inteiro(notas)
    s = 0
    m = 0
    for xs in range(0,xs):
        n = real('Informe as notas ')
        s = (s +n)
        m = s/(xs+1)
    return m
