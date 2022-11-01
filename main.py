import Estudante
import numeros, Pessoa,char


p = Estudante.Estudante(nome=char.char('Nome '),
           nasc = numeros.inteiro('Seu nascimento '),
           sexo = char.sexo('Sexo[M/F] '), aluno = False,
            av = numeros.av('Total de avaliações '))

p.dados()




