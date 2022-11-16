import Estudante
import numeros, Pessoa,char

list = []
xs = numeros.inteiro('Cadastro ')
print('-'*50)
for c in range (xs):
    op = char.opção()
    if op == 1:
        p1 = Estudante.Estudante(nome=char.char('Nome ').title(),
                                nasc=numeros.inteiro('Seu nascimento '),
                                sexo=char.sexo('Sexo[M/F] '),idade=(),
                                aluno=char.char('Aluno '),
                                 av= numeros.av('Avaliações '))
        print('-' * 50)
        list.append(p1.__dict__.copy())
    elif op ==5:
        p = Pessoa.Pessoa(nome=char.char('Nome ').title(),
                   nasc = numeros.inteiro('Seu nascimento '),idade=(),
                   sexo = char.sexo('Sexo[M/F] '))
        print('-'*50)
        list.append(p.__dict__.copy())
print(list)




