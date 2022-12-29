import numeros, Pessoa,char, Estudante,Funcionario,Estagiario,Professor
import time
import datetime as dt
from arquivos import *


jan = 'Teste.txt'#arquivo a ser procurado ou criado
now = dt.datetime.now()#variável da data atual
list = ['Cadastro(s) resumido(s) ']#lista que será guardada

if existir(jan):#Procura a existência do arquivo
    print(f'Arquivo Encontrado')
else:
    print(f'Arquivo não encontrado')
    createfile(jan)#cria o arquivo inexistente

print('-'*100)
print(now.strftime('%a,%d,%B,%Y'))#data formatada em semana, dia, mês e ano
print(now.strftime('%H:%M:%S'))#horário formatado
print('-'*100)

xs = numeros.inteiro('Cadastro ')#vai definir quantos cadastros
print('-'*100)
ces , ct , cf , cp, cv = 0,0,0,0,0# contadores zerados de cada categoria
sm , sf = 0 , 0 # inicia a contabilização dos sexo masculino e feminino

for c in range (xs):#vai pedir com qual tipo de cadastro quer realizar
    op = char.opção('Estudante[1]/Estagiário[2]/Funcionário[3]/Professor[4]/Visitante[5] ')
    print('-'*100)
    if op == 1:
        c += 1#numeração do cadastro a ser realizado
        print(f'Cadastro {c}'.center(100))
        ces+=1
        print(f'Estudante'.center(100))
        p = Estudante.Estudante('Estudante',nome=char.char('Nome ').title(),#entrada de dados do Estudante
                                nasc= numeros.inteiro('Nascimento '),idade=(),
                                sexo=char.sexo('Sexo[M/F] '),aluno=char.aluno('Aluno[S/N] '),#resposta Sim ou Não
                                 av= numeros.av('Avaliações '))
        if p.sexo in 'Mm':#Contabiliza qual sexo do usuário inserido
            sm+=1
            continue
        else:
            sf+=1
        list.append(p.__dict__.copy())#lista adicionada pelo dicionário
        p.write(jan, p.__str__())#escreve os dados do usuário no arquivo
        time.sleep(0.4)#tempo de espera de 4 segundos
        p.dados()#apresentação dos dados incluidos
        print('-'*100)
    elif op == 2:
        c += 1
        print(f'Cadastro {c}'.center(100))
        print(f'Estagiário'.center(100))
        ct +=1
        p2 = Estagiario.Estagiario('Estagiário',nome=char.char('Nome ').title(),#entrada de dados do estagiário
                   nasc = numeros.inteiro('Nascimento '),idade=(),sexo = char.sexo('Sexo[M/F] '),
                    tempo = numeros.real('Tempo de contrato '),horas = numeros.real('Horas diárias '),
                    carga = numeros.real('Horas semanais '),periodo = char.periodo('Período[M/T/N] ').strip().upper()[0],
                    b_aux= numeros.real('Bolsa auxilio R$ '),noturno=())
        if p2.sexo in 'Mm':
            sm+=1
            continue
        else:
            sf+=1
        list.append(p2.__dict__.copy())
        p2.write(jan,p2.__str__())
        p2.dados()
        time.sleep(0.4)
        print('-'*100)
    elif op == 3:
        c += 1
        print(f'Cadastro {c}'.center(100))
        print(f'Funcionário'.center(100))
        cf +=1
        p3 = Funcionario.Funcionario('Funcionário',nome = char.char('Nome ').title(),nasc = numeros.inteiro('Nascimento '),
                                     idade=(),sexo=char.sexo('Sexo[M/F] '),funcao = char.char('Função ').title(),
                                     salario = numeros.real('Salário '),tempo=numeros.real('Horas diárias '),
                                     carga=numeros.real('Horas semanais '),exp=numeros.real('Tempo na empresa '),
                                     desc=numeros.inteiro('Desconto(-) '),plus=numeros.inteiro('Aumento(+) '),
                                     novo=(),atual=())
        if p3.sexo in 'Mm':
            sm+=1
            continue
        else:
            sf+=1
        list.append(p3.__dict__.copy())
        p3.write(jan,p3.__str__())
        time.sleep(0.4)
        p3.dados()
        print('-'*100)
    elif op == 4:
        c += 1
        print(f'Cadastro {c}'.center(100))
        print(f'Professor'.center(100))
        cp +=1
        p4 = Professor.Professor('Professor', nome=char.char('Nome ').title(), nasc=numeros.inteiro('Nascimento '),
                                 idade=(), sexo=char.sexo('Sexo[M/F] '), materia=char.char('Matéria '),
                                 salario=numeros.real('Salário '), tempo=numeros.real('Horas diárias '),
                                 carga=numeros.real('Horas semanais '), exp=numeros.real('Tempo na empresa '),
                                 desc=numeros.inteiro('Desconto(-) '), plus=numeros.inteiro('Aumento(+) '),
                                 novo=(), atual=())
        if p4.sexo in 'Mm':
            sm+=1
            continue
        else:
            sf+=1
        list.append(p4.__dict__.copy())
        p4.write(jan,p4.__str__())
        time.sleep(0.4)
        p4.dados()
        print('-'*100)
    elif op == 5:
        c += 1
        print(f'Cadastro {c}'.center(100))
        print(f'Visitante'.center(100))
        cv+=1
        p5 = Pessoa.Pessoa('Visitante',nome=char.char('Nome ').title(),#entrada de dados do visitante
                   nasc = numeros.inteiro('Nascimento '),idade=(),sexo = char.sexo('Sexo[M/F] '))
        if p5.sexo in 'Mm':
            sm+=1
            continue
        else:
            sf+=1
        list.append(p5.__dict__.copy())#lista adicionada pelo dicionário
        p5.write(jan, p5.__str__())
        time.sleep(0.4)
        p5.dados()
        print('-'*100)
        time.sleep(0.6)

ll = 0
for ll in list:
    print(ll)#retorna cada cadastro localizado na lista

time.sleep(0.6)#tempo de espera de 6 segundos
print('-'*100)
print(f'Cadastro(s) total(is) {xs}')#apresentação dos cadastros totais
print(f'Estudante(s) {ces}, Estagiário(s) {ct}, Funcionário(s) {cf}, Professor(es) {cp}, Visitante(s) {cv}')
#visualização do somatório de cada cadastro
print('-'*100)
print(f'Sexo Masculino {sm}                Sexo Feminino {sf}'.center(80))#contabilização total de cadastros do sexo
# masculino e feminino
