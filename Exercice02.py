# Classificação até 16 anos: Menor, 16 a 18 anos: Emancipado, Maiores de 18 anos: Maior
idade = int(input("Qual a idade do aluno: "))

if idade <= 16:
    print("O Aluno tem {} anos:MENOR".format(idade))

elif idade >= 16:
    print("O Aluno tem {} anos:EMANCIPADO".format(idade))

else:
    print("O Aluno tem {} anos:MAIOR".format(idade))
