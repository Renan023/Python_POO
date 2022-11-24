def inteiro(n):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mDigite um número válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mInterrompido pelo usuário\033[m')
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
    xs = inteiro(notas)#definir quantas avaliações
    s = 0
    m = 0
    for xs in range(0,xs):#definir quantas notas
        n = real('Informe as notas ')
        s = (s +n)#soma das avaliações
        m = s/(xs+1)#divisão da soma de avaliações e valor total definido por xs +1(já que a contagem começa do 0 o +1 só ajusta o valor)
    return m

