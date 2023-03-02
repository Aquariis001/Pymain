"""

Como achar factorial de um número

"""
numero = int(input('Insira um numero: '))

factorial = 1
if numero < 0:
    print("Não existe fatorial de numeros negativos")
elif numero == 0:
    print(f'O fatorial de {numero} é de 1')
else:
    for x in range(1, numero+1):
        factorial = factorial * x  # (factorial *= x) funciona do mesmo jeito.
        print(f'O fatorial de {numero} é : {factorial}')
