

def existir(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createfile(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print(f'Erro na criação do arquivo')
    else:
        print(f'{nome} criado com sucesso ')


def readfile(name):
    try:
        a = open(name,'rt')
    except:
        print(f'Erro na leitura do arquivo')
    else:
        print(a.read())


