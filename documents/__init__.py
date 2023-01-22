from char import *

def rg(rg):
    while True:
        try:

            rg = char(rg)

            while len(rg) != 9:
                print(f'\033[31mRG inválido\033[m')
                rg = char('RG ')
                if len(rg)!= 10:
                    print(f'\033[34mRG {rg} aceito\033[m')
        except (KeyboardInterrupt):
            print(f'\033[31mInterrompido pelo usuário\033[m')
        else:
            return rg


def cpf(cpf):
    while True:
        try:
            cpf = char(cpf)
            while len(cpf) != 11:
                print(f'\033[31mCPF inválido\033[m')
                cpf = char('CPF ')

            s = 0
            r = 11
            for c in range(0,9):
                r-=1
                s+= int(cpf)*r
                mod1 = s%11
                if mod1 == 0:
                    dig1 = mod1
                else:
                    dig1 =11-mod1
                    if dig1>=10:
                        fdig = 0
                    else:
                        fdig = dig1

            r1 = 11
            s1= 0
            for c in range(0,9):
                r1-=1
                s1+=int(cpf)*r1
                mod2 = s%11
                if mod2 == 0:
                    dig2 = mod2
                else:
                    dig2 = 11 - mod2
                    if dig2 >=10:
                        sdig = 0
                    else:
                        sdig = mod2

            if int(cpf[9:10])==fdig or int(cpf[10:11]) == sdig:
                print(f'\033[34mCPF {cpf} aceito\033[m')
        except(KeyboardInterrupt):
            print(f'\033[31mInterrompido pelo usuário\033[m')
        else:
            return cpf