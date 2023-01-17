import Pessoa, Estudante,Funcionario,Estagiario,Professor, time
import datetime as dt
from arquivos import *
from char import *


student, intern, employee, teacher, visitor = 'student.csv','intern.csv','employee.csv','teacher.csv','visitor.csv'#arquivo a ser procurado ou criado
now = dt.datetime.now()#variável da data atual
list = ['Cadastro(s) resumido(s) ']#lista que será guardada


line()
print(now.strftime('%a,%d,%B,%Y'))#data formatada em semana, dia, mês e ano
print(now.strftime('%H:%M:%S'))#horário formatado
line()

xs = inteiro('Cadastro ')#vai definir quantos cadastros
print('-'*100)
ces , ct , cf , cp, cv = 0,0,0,0,0# contadores zerados de cada categoria
sm , sf = 0 , 0 # inicia a contabilização dos sexo masculino e feminino

for c in range (xs):#vai pedir com qual tipo de cadastro quer realizar
    op = opção('Estudante[1]/Estagiário[2]/Funcionário[3]/Professor[4]/Visitante[5] ')
    print('-'*100)
    if op == 1:
        c += 1#numeração do cadastro a ser realizado
        if existir(student):  # Procura a existência do arquivo
            print(f'Arquivo Encontrado')
        else:
            print(f'Arquivo não encontrado')
            createfile(student)  # cria o arquivo inexistente
        print(f'Cadastro {c}'.center(100))
        ces+=1
        category('Estudante')
        p = Estudante.Estudante(nome=char('Nome ').title(),#entrada de dados do Estudante
                                nasc= inteiro('Nascimento '),idade=(),
                                sexo=sexo('Sexo[M/F] '),aluno=aluno('Aluno[S/N] '),#resposta Sim ou Não
                                 av= av('Avaliações '))
        if p.sexo in 'Mm':#Contabiliza qual sexo do usuário inserido
            sm+=1
        else:
            sf+=1
        list.append(p.__dict__.copy())#lista adicionada pelo dicionário
        p.write(student, p.__str__())#escreve os dados do usuário no arquivo
        time.sleep(0.4)#tempo de espera de 4 segundos
        p.dados()#apresentação dos dados incluidos
        line()
    elif op == 2:
        c += 1
        if existir(intern):  # Procura a existência do arquivo
            print(f'Arquivo Encontrado')
        else:
            print(f'Arquivo não encontrado')
            createfile(intern)  # cria o arquivo inexistente

        print(f'Cadastro {c}'.center(100))
        category('Estagiário')
        ct +=1
        p2 = Estagiario.Estagiario(nome=char('Nome ').title(),#entrada de dados do estagiário
                   nasc = inteiro('Nascimento '),idade=(),sexo = sexo('Sexo[M/F] '),
                    tempo = real('Tempo de contrato '),horas = real('Horas diárias '),
                    carga = real('Horas semanais '),periodo = periodo('Período[M/T/N] ').strip().upper()[0],
                    b_aux= real('Bolsa auxilio R$ '),noturno=())
        if p2.sexo in 'Mm':
            sm+=1
        else:
            sf+=1
        list.append(p2.__dict__.copy())
        p2.write(intern,p2.__str__())
        p2.dados()
        time.sleep(0.4)
        line()
    elif op == 3:
        c += 1
        if existir(employee):  # Procura a existência do arquivo
            print(f'Arquivo Encontrado')
        else:
            print(f'Arquivo não encontrado')
            createfile(employee)  # cria o arquivo inexistente
        print(f'Cadastro {c}'.center(100))
        category('Funcionário')
        cf +=1
        p3 = Funcionario.Funcionario(nome = char('Nome ').title(),nasc = inteiro('Nascimento '),
                                     idade=(),sexo=sexo('Sexo[M/F] '),funcao = char('Função ').title(),
                                     salario = real('Salário '),tempo=real('Horas diárias '),
                                     carga=real('Horas semanais '),exp=real('Tempo na empresa '),
                                     desc=inteiro('Desconto(-) '),plus=inteiro('Aumento(+) '),
                                     novo=(),atual=())
        if p3.sexo in 'Mm':
            sm+=1
        else:
            sf+=1
        list.append(p3.__dict__.copy())
        p3.write(employee,p3.__str__())
        time.sleep(0.4)
        p3.dados()
        line()
    elif op == 4:
        c += 1
        if existir(teacher):  # Procura a existência do arquivo
            print(f'Arquivo Encontrado')
        else:
            print(f'Arquivo não encontrado')
            createfile(teacher)  # cria o arquivo inexistente
        print(f'Cadastro {c}'.center(100))
        category('Professor')
        cp +=1
        p4 = Professor.Professor(nome=char('Nome ').title(), nasc=inteiro('Nascimento '),
                                 idade=(), sexo=sexo('Sexo[M/F] '), materia=char('Matéria '),
                                 salario=real('Salário '), tempo=real('Horas diárias '),
                                 carga=real('Horas semanais '), exp=real('Tempo na empresa '),
                                 desc=inteiro('Desconto(-) '), plus=inteiro('Aumento(+) '),
                                 novo=(), atual=())
        if p4.sexo in 'Mm':
            sm+=1
        else:
            sf+=1
        list.append(p4.__dict__.copy())
        p4.write(teacher,p4.__str__())
        time.sleep(0.4)
        p4.dados()
        line()
    elif op == 5:
        c += 1
        print(f'Cadastro {c}'.center(100))
        category('Visitante')
        cv+=1
        if existir(visitor):  # Procura a existência do arquivo
            print(f'Arquivo Encontrado')
        else:
            print(f'Arquivo não encontrado')
            createfile(visitor)  # cria o arquivo inexistente
        p5 = Pessoa.Pessoa(nome=char('Nome ').title(),#entrada de dados do visitante
                   nasc = inteiro('Nascimento '),idade=(),sexo = sexo('Sexo[M/F] '))
        if p5.sexo in 'Mm':
            sm+=1
        else:
            sf+=1
        list.append(p5.__dict__.copy())#lista adicionada pelo dicionário
        p5.write(visitor, p5.__str__())
        time.sleep(0.4)
        p5.dados()
        line()
        time.sleep(0.6)

ll = 0
for ll in list:
    print(ll)#retorna cada cadastro localizado na lista

time.sleep(0.6)#tempo de espera de 6 segundos
line()
print(f'Cadastro(s) total(is) {xs}')#apresentação dos cadastros totais
print(f'Estudante(s) {ces}, Estagiário(s) {ct}, Funcionário(s) {cf}, Professor(es) {cp}, Visitante(s) {cv}')
#visualização do somatório de cada cadastro
line()
print(f'Sexo Masculino {sm}                Sexo Feminino {sf}'.center(80))#contabilização total de cadastros do sexo
# masculino e feminino