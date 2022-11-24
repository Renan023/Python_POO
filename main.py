import numeros, Pessoa,char, Estudante,Funcionario

list = []
xs = numeros.inteiro('Cadastro ')#vai definir quantos cadastros
print('-'*100)
for c in range (xs):
    op = char.opção('Estudante[1]/Estagiário[2]/Funcionário[3]/Professor[4]/Visitante[5] ')#entrada da opção se estudante, visitante .....
    print('-'*100)
    if op == 1:
        p = Estudante.Estudante(nome=char.char('Nome ').title(),#entrada de dados do Estudante
                                nasc= numeros.inteiro('Nascimento '),idade=(),
                                sexo=char.sexo('Sexo[M/F] '),aluno=char.aluno('Aluno[S/N] '),#resposta Sim ou Não
                                 av= numeros.av('Avaliações '))
        print('-' * 100)
        list.append(p.__dict__.copy())#lista adicionada pelo dicionário
    elif op == 3:
        p3 = Funcionario.Funcionario(nome = char.char('Nome ').title(),nasc = numeros.inteiro('Nascimento '),
                                     idade=(),sexo=char.sexo('Sexo[M/F] '),funcao = char.char('Função ').title(),
                                     salario = numeros.real('Salário '),tempo=numeros.real('Horas diárias '),
                                     carga=numeros.real('Horas semanais '),exp=numeros.real('Tempo na empresa '),
                                     desc=numeros.inteiro('Desconto(-) '),plus=numeros.inteiro('Aumento(+) '),novo=(),atual=())
        print('-'*100)
        list.append(p3.__dict__.copy())
    elif op == 5:
        p5 = Pessoa.Pessoa(nome=char.char('Nome ').title(),#entrada de dados do visitante
                   nasc = numeros.inteiro('Nascimento '),idade=(),sexo = char.sexo('Sexo[M/F] '))
        print('-'*100)
        list.append(p5.__dict__.copy())#lista adicionada pelo dicionário
print(list)




