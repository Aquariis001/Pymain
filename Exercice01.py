"""
Exercicios Matematicos

01 - área e um retângulo (feito)
02 - área de um quadrado (feito)
03 - Se o produto que você quer avaliar custa (??) reais qual será do mesmo valor com desconto de (??)%
04 - área de um círculo (feito)
05 - conversão de reais para dollar (feito)
06 - conversão de dolar para reais (feito)

"""
"""
# Exerc 01 - area do retângulo
print('-='*30)

base = input("Qual o tamanho da base do retângulo: ")
altura = input("Qual o tamanho da altura do retângulo: ")

print('-='*30)

area = float(base) * float(altura)

print(f"A área do retangulo é de: {area} unidade de medida")

print('-='*30)

# Exerc 02 - area do quadradro


def f():
    print('-='*30)

    base = input('Qual o tamanho da base do seu quadrado: ')
    altura = input('Qual o tamanho da altura do seu quadrado: ')

    print('-='*30)

    area = float(base) * float(altura)
    print(f'Calculando a altura e a base a área do seu quadrado é de: {area}')
    print('-='*30)


f()


def c():
    print('-='*30)

    base = input('Qual o tamanho da base do seu circulo: ')
    altura = input('Qual o tamanho da altura do seu circulo: ')
    area = float(base) * float(altura)

    print('-='*30)

    print(f'A área do seu circulo é de: {area}')

    print('-='*30)


c()



def d():

    real = float(input('Quanto dejesa converter em dollar: '))
    dollar = 5.19
    convert = (real / dollar)
    print('Voce tem em {:.2f} dollares'.format(convert))


d()

x = a


def r():

    dollar = float(input('Quanto dollares você quer converter: '))
    real = 5.19

    convert = (dollar * real)

    print(
        'Seus dollares foram convertidos em reais e você tem R${:.2f}.'.format(x))


r()

"""
