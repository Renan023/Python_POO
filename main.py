import Pessoa, Estudante,Funcionario,Estagiario,Professor

import datetime as dt
from arquivos import *
import mysql.connector
from documents import *
from communication import *


con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cadastro',
)
cur = con.cursor()

student, intern, employee, teacher, visitor = 'student.csv','intern.csv','employee.csv','teacher.csv','visitor.csv'#arquivo a ser procurado ou criado
now = dt.datetime.now()#variável da data atual
list = ['Cadastro(s) resumido(s) ']#lista que será guardada
remetente = ''
senha = "blljijnqaqqteaer"

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
        p = Estudante.Estudante(nome=char('Nome ').title(),rg = rg('RG '),cpf = cpf('CPF '),
                                phone= phone('Telefone/WPP '),email = email('E-mail '),
                                nasc= inteiro('Nascimento '),idade=(),sexo=sexo('Sexo[M/F] '),
                                aluno=aluno('Aluno[S/N] '),#resposta Sim ou Não
                                av= av('Avaliações '))
        if p.sexo in 'Mm':#Contabiliza qual sexo do usuário inserido
            sm+=1
        else:
            sf+=1
        command = f'insert into student(Nome,RG,CPF,Telefone,Email,Nasc,Idade,Sexo,Aluno,Avaliacao) values ' \
                  f'("{p.nome}","{p.rg}","{p.cpf}","{p.phone}","{p.email}","{p.nasc}","{p.idade}","{p.sexo}",' \
                  f'"{p.aluno}","{p.av}")\n'
        cur.execute(command)
        con.commit()
        list.append(p.__dict__.copy())#lista adicionada pelo dicionário
        p.write(student, p.__str__())#escreve os dados do usuário no arquivo
        time.sleep(0.4)#tempo de espera de 4 segundos
        p.send_mail(p.nome,remetente,p.email)
        p.dados()#apresentação dos dados incluidos
        p.wpp()
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
        p2 = Estagiario.Estagiario(nome=char('Nome ').title(),rg = rg('RG '),cpf = cpf('CPF ')
                                   ,phone= phone('Telefone/WPP '),email = email('E-mail '),
                                    nasc = inteiro('Nascimento '),idade=(),sexo = sexo('Sexo[M/F] '),
                                    tempo = real('Tempo de contrato '),horas = real('Horas diárias '),
                                    carga = real('Horas semanais '),periodo = periodo('Período[M/T/N] ').strip().upper()[0],
                                    b_aux= real('Bolsa auxilio R$ '),noturno=())
        if p2.sexo in 'Mm':
            sm+=1
        else:
            sf+=1
        command = f'insert into intern (Nome,RG,CPF,Telefone,Email,Nasc,Idade,Sexo,Contrato,Diarias,Semanais,' \
                  f'Periodo,Bolsa_aux,Total) values("{p2.nome}","{p2.rg}","{p2.cpf}","{p2.phone}","{p2.email}",' \
                  f'"{p2.nasc}","{p2.idade}","{p2.sexo}","{p2.tempo}","{p2.horas}","{p2.carga}","{p2.periodo}",' \
                  f'"{p2.b_aux}","{p2.noturno}")\n'
        cur.execute(command)
        con.commit()
        list.append(p2.__dict__.copy())
        p2.write(intern,p2.__str__())
        p2.dados()
        time.sleep(0.4)
        p2.send_mail(p2.nome,remetente,p2.email)
        p2.wpp()
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
        p3 = Funcionario.Funcionario(nome = char('Nome ').title(),rg = rg('RG '),cpf = cpf('CPF '),
                                     phone= phone('Telefone/WPP '),email = email('E-mail '),
                                     nasc = inteiro('Nascimento '),idade=(),sexo=sexo('Sexo[M/F] '),
                                     funcao = char('Função ').title(),salario = real('Salário '),
                                     tempo=real('Horas diárias '),carga=real('Horas semanais '),
                                     exp=real('Tempo na empresa '),desc=inteiro('Desconto(-) '),
                                     plus=inteiro('Aumento(+) '),novo=(),atual=())
        if p3.sexo in 'Mm':
            sm+=1
        else:
            sf+=1
        command = f'insert into employee (Nome,RG,CPF,Telefone,Email,Nasc,Idade,Sexo,Funcao,Salario,Diarias,Semanais,Empresa,' \
                  f'Desconto,Acrescimo,Novo,Total) values ("{p3.nome}","{p3.rg}","{p3.cpf}","{p3.phone}","{p3.email}",' \
                  f'"{p3.nasc}","{p3.idade}","{p3.sexo}","{p3.funcao}","{p3.salario}","{p3.tempo}","{p3.carga}",' \
                  f'"{p3.exp}","{p3.desc}","{p3.plus}","{p3.novo}","{p3.atual}")\n'
        cur.execute(command)
        con.commit()
        list.append(p3.__dict__.copy())
        p3.write(employee,p3.__str__())
        time.sleep(0.4)
        p3.send_mail(p3.nome, remetente, p3.email)
        p3.dados()
        p3.wpp()
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
        p4 = Professor.Professor(nome=char('Nome ').title(),rg = rg('RG '),cpf = cpf('CPF '),
                                 phone= phone('Telefone/WPP '),email = email('E-mail '),
                                 nasc=inteiro('Nascimento '),idade=(), sexo=sexo('Sexo[M/F] '),
                                 materia=char('Matéria '),salario=real('Salário '), tempo=real('Horas diárias '),
                                 carga=real('Horas semanais '), exp=real('Tempo na empresa '),
                                 desc=inteiro('Desconto(-) '), plus=inteiro('Aumento(+) '),
                                 novo=(), atual=())
        command = f'insert into teacher (Nome,RG,CPF,Telefone,Email,Nasc,Idade,Sexo,Materia,Salario,Diarias,Semanais,' \
                  f'Empresa,Desconto,Acrescimo,Novo,Total) values("{p4.nome}","{p4.rg}","{p4.cpf}","{p4.phone}","{p4.email}",' \
                  f'"{p4.nasc}","{p4.idade}","{p4.sexo}","{p4.materia}","{p4.salario}","{p4.tempo}","{p4.carga}","{p4.exp}",' \
                  f'"{p4.desc}","{p4.plus}","{p4.novo}","{p4.atual}")\n'
        cur.execute(command)
        con.commit()
        if p4.sexo in 'Mm':
            sm+=1
        else:
            sf+=1
        list.append(p4.__dict__.copy())
        p4.write(teacher,p4.__str__())
        time.sleep(0.4)
        p4.send_mail(p4.nome,remetente,p4.email)
        p4.dados()
        p4.wpp()
        line()
    elif op == 5:
        c += 1
        if existir(visitor):  # Procura a existência do arquivo
            print(f'Arquivo Encontrado')
        else:
            print(f'Arquivo não encontrado')
            createfile(visitor)  # cria o arquivo inexistente
        print(f'Cadastro {c}'.center(100))
        category('Visitante')
        cv+=1
        p5 = Pessoa.Pessoa(nome=char('Nome ').title(),#entrada de dados do visitante
                           rg = rg('RG '),cpf = cpf('CPF '),phone= phone('Telefone/WPP '),
                           email = email('E-mail '),nasc = inteiro('Nascimento '),
                           idade=(),sexo = sexo('Sexo[M/F] '))
        if p5.sexo in 'Mm':
            sm+=1
        else:
            sf+=1
        command = f'insert into visitor (Nome,RG,CPF,Telefone,Email,Nasc,Idade,Sexo) values ' \
                  f'("{p5.nome}","{p5.rg}","{p5.cpf}","{p5.phone}","{p5.email}",' \
                  f'"{p5.nasc}","{p5.idade}","{p5.sexo}")\n'
        cur.execute(command)
        con.commit()
        list.append(p5.__dict__.copy())#lista adicionada pelo dicionário
        p5.write(visitor,p5.__str__())
        time.sleep(0.4)
        p5.send_mail(p5.nome,remetente,p5.email)
        p5.dados()
        p5.wpp()
        time.sleep(10)
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
agradecimento()