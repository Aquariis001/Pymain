''' Classificação até 16 anos: Menor, 16 a 18 anos: Emancipado, Maiores de 18 Anos : Maior'''
idade = int(input("Qual a idade do aluno: "))

if idade <= 16:
    print(f"O Aluno tem {idade} anos:MENOR")
    if idade == [5, 6, 7]:
        print('O aluno foi qualificado como: Infantil A')
    elif idade == (7, 8, 9, 10, 11):
        print('O aluno foi qualificado como: Infantil B')
elif idade >= 12:
    print(f"O Aluno tem {idade} anos:EMANCIPADO")
    if idade == (12, 13, 14):
        print('O Aluno foi clasificado como: Juvenil A')
    elif idade == (15, 16, 17):
        print('O Aluno foi clasificado como: Juvenil B')
else:
    print(f"O Aluno tem {idade} anos:MAIOR")

