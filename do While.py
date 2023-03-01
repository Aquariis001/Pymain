"""

do while

Código para adivinhar um número

"""

palpite = 0
numero = 9

while True:  # Nós executamos sem verificar
    print("Qual é o numero correto? ")
    palpite = int(input())
    if palpite == numero:  # Estamos verificando nosso código
        print('Parabens você acertou!!')
        break
    else:
        print('Você errou...')

else:
    print('Erro na aplicação')
    print(bool(palpite))
