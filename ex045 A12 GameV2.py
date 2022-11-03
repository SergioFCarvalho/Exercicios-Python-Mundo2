# GAME: Pedra Papel e Tesoura
from time import sleep
from random import randint
print('\033[1m<<<<<<< JOKENPÔ V2.0 >>>>>>>>>>\033[m')
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
itens = ('Pedra','Papel','Tesoura')
computer = randint(0, 2)
jogador = int(input('Qual sua jogada? '))
if jogador > 2:
    print('Jogada Inválida!!!')
    exit()
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-=' * 7)
print(f'Computador jogou {itens[computer]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=-=' * 7)
if computer == 0:  # Computador jogou Pedra
    if jogador == 0:
        print('EMPATE!!!')
    elif jogador == 1:
        print('Jogador Vence!!!')
    elif jogador == 2:
        print('Computador Vence!!!')

elif computer == 1: # Computador jogou Papel
    if jogador == 0:
        print('Computador Vence!!!')
    elif jogador == 1:
        print('EMPATE!!!')
    elif jogador == 2:
        print('Jogador Vence!!!')

elif computer == 2:  # Computador jogou Tesoura
    if jogador == 0:
        print('Jogador Vence!!!')
    elif jogador == 1:
        print('Computador Vence!!!')
    elif jogador == 2:
        print('EMPATE!!!')

