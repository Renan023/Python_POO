import numeros, Pessoa,char, Estudante,Funcionario,Estagiario,Professor
import time, datetime

list = ['Cadastro(s) resumido(s) ']
print(datetime.datetime.today().replace())
xs = numeros.inteiro('Cadastro ')#vai definir quantos cadastros
print('-'*100)
ces , ct , cf , cp, cv = 0,0,0,0,0# contadores zerados de cada categoria
for c in range (xs):
    op = char.opção('Estudante[1]/Estagiário[2]/Funcionário[3]/Professor[4]/Visitante[5] ')#entrada da opção se estudante, visitante .....
    print('-'*100)
    if op == 1:
        c += 1
        print(f'Cadastro {c}'.center(100))
        ces+=1
        print(f'Estudante'.center(100))
        p = Estudante.Estudante(nome=char.char('Nome ').title(),#entrada de dados do Estudante
                                nasc= numeros.inteiro('Nascimento '),idade=(),
                                sexo=char.sexo('Sexo[M/F] '),aluno=char.aluno('Aluno[S/N] '),#resposta Sim ou Não
                                 av= numeros.av('Avaliações '))
        list.append(p.__dict__.copy())#lista adicionada pelo dicionário
        time.sleep(0.4)
        p.dados()
        print('-'*100)
    elif op == 2:
        c += 1
        print(f'Cadastro {c}'.center(100))
        print(f'Estagiário'.center(100))
        ct +=1
        p2 = Estagiario.Estagiario(nome=char.char('Nome ').title(),#entrada de dados do visitante
                   nasc = numeros.inteiro('Nascimento '),idade=(),sexo = char.sexo('Sexo[M/F] '),
                    tempo = numeros.real('Tempo de contrato '),horas = numeros.real('Horas diárias '),
                    carga = numeros.real('Horas semanais '),periodo = char.periodo('Período[M/T/N] ').strip().upper()[0],
                    b_aux= numeros.real('Bolsa auxilio R$ '))
        list.append(p2.__dict__.copy())
        p2.dados()
        time.sleep(0.4)
        print('-'*100)
    elif op == 3:
        c += 1
        print(f'Cadastro {c}'.center(100))
        print(f'Funcionário'.center(100))
        cf +=1
        p3 = Funcionario.Funcionario(nome = char.char('Nome ').title(),nasc = numeros.inteiro('Nascimento '),
                                     idade=(),sexo=char.sexo('Sexo[M/F] '),funcao = char.char('Função ').title(),
                                     salario = numeros.real('Salário '),tempo=numeros.real('Horas diárias '),
                                     carga=numeros.real('Horas semanais '),exp=numeros.real('Tempo na empresa '),
                                     desc=numeros.inteiro('Desconto(-)'),plus=numeros.inteiro('Aumento(+) '),
                                     novo=(),atual=())
        list.append(p3.__dict__.copy())
        time.sleep(0.4)
        p3.dados()
        print('-'*100)
    elif op == 4:
        c += 1
        print(f'Cadastro {c}'.center(100))
        print(f'Professor'.center(100))
        cp +=1
        p4 = Professor.Professor(nome = char.char('Nome ').title(),nasc = numeros.inteiro('Nascimento '),
                                     idade=(),sexo=char.sexo('Sexo[M/F] '),funcao = char.char('Função ').title(),
                                     salario = numeros.real('Salário '),tempo=numeros.real('Horas diárias '),
                                     carga=numeros.real('Horas semanais '),exp=numeros.real('Tempo na empresa '),
                                     desc=numeros.inteiro('Desconto(-)'),plus=numeros.inteiro('Aumento(+) '),
                                     novo=(),atual=(),materia=('Matéria '))
        list.append(p4.__dict__.copy)
        time.sleep(0.4)
        p4.dados()
        print('-'*100)
    elif op == 5:
        c += 1
        print(f'Cadastro {c}'.center(100))
        print(f'Visitante'.center(100))
        cv+=1
        p5 = Pessoa.Pessoa(nome=char.char('Nome ').title(),#entrada de dados do visitante
                   nasc = numeros.inteiro('Nascimento '),idade=(),sexo = char.sexo('Sexo[M/F] '))
        list.append(p5.__dict__.copy())#lista adicionada pelo dicionário
        time.sleep(0.4)
        p5.dados()
        print('-'*100)
        time.sleep(0.6)

print(list)
"""cad = {f'Cadastro {xs} ': pd.Series([list],index=[xs])}
res = pd.DataFrame(cad)
print(res)"""

print(f'Cadastro(s) total(is) {xs}')
print(f'Estudante(s) {ces}, Estagiário(s) {ct}, Funcionário(s) {cf}, Professor(es) {cp}, Visitante(s) {cv}')
