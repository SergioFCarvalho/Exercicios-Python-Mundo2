# 58 – Jogo da Adivinhação v2.0
'''from random import randint
print('Souuu seu computador.....
Pensei em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
computador = randint(0, 10)
palpites = 1
jogador = 1
while computador != jogador:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador > computador:
       # print('Menos...tente novamente.')
    elif jogador < computador:
        #print('Mais...Tente outra vez.')
    elif jogador == computador:
        print(f'Acertou com {palpites} tentativas.Parabéns!!!')
'''
# Abaixo outra forma de fazer esse jogo da Advinhação
from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\033[32mQual seu palpite?\033[m'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos...Tente outra vez.')
        elif jogador < computador:
            print('Mais...Tente outra vez.')
print(f'Acertou com {palpites} tentativas.Parabens!!!')