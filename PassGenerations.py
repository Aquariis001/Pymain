
# maiúsculas e minúsculas
# símbolos e espaços

"""
Securíty = Chave
53crt1ty = senha

hex

1=1
2=2
até 9=9
10 = A
11 = B
12 = C
13 = D
14 = F

"""

chave = input('Digite a base de sua senha: ')

senha = ""
for letra in chave:
    if letra in "Aa":
        senha = senha + "10"
    elif letra in "Bb":
        senha = senha + "1"
    elif letra in "Cc":
        senha = senha + "9"
    elif letra in "Dd":
        senha = senha + "@"
    elif letra in "Ee":
        senha = senha + "69"
    elif letra in "Ff":
        senha = senha + "15"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "%"
    elif letra in "Mm":
        senha = senha + "$"
    elif letra in "Nn":
        senha = senha + "$"
    elif letra in "Oo":
        senha = senha + "3"
    elif letra in "Ii":
        senha = senha + "0"
print(senha)
