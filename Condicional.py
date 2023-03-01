"""

Operadores Ternais

"""
"""
x = 3
y = 3

if y > x:
    print("y é maior que x")
    print("Código dentro do bloco condicional")

elif y < x:
    print("y é menor que x")

elif y == x:
    print("y é igual a x")


else:
    print("y é menor ou igual a x")
    print(y > x)
"""


a = 5
b = 8
c = 3
"""

if b > a:
    print('b é maior que a')
print('codigo fora do bloco if')

"""

"""
print("B") if b > a else print("A") # Operador Ternário
"""

if a > b:
    print('A')
    if a > c:
        print('A')       
