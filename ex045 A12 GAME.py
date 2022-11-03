# GAME: Pedra Papel e Tesoura
from time import sleep
from random import randint
print('         \033[3;31m>>>>>> GAME - JOKENPÔ V 1.0 <<<<<<<<<\033[m      ')
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua jogada? '))
computer = (randint(0, 2))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=-=-=' * 20)
    # Condições se jogador jogar apenas número 0
if jogador == 0:
    print('Jogador jogou Pedra')
    if computer == 0:
        print('Computador jogou Pedra')
        print('EMPATE!!!')
    elif computer == 1:
        print('Computador jogou Papel')
        print('\033[4;31mComputador Venceu!!!\033[m')
    elif computer == 2:
        print('Computador jogou Tesoura')
        print('\033[3;32mJogador Venceu!!\033[m')
    #Condições se jogador jogar apenas número 1
if jogador == 1:
    print('Jogador jogou Papel')
    if computer == 0:
        print('Computador jogou Pedra')
        print('\033[3;32mJogador Venceu!!\033[m')
    elif computer == 1:
        print('Computador jogou Papel')
        print('EMPATE!!!')
    elif computer == 2:
        print('Computador jogou Tesoura')
        print('\033[4;31mComputador Venceu!!!!\033[m')
    # Condições se jogador jogar apenas 2
if jogador == 2:
    print('Jogador jogou Tesoura')
    if computer == 0:
        print('Computador jogou Pedra')
        print('\033[4;31mComputador Venceu!!\033[m')
    elif computer == 1:
        print('Computador jogou Papel')
        print('\033[3;32mJogador Venceu!!\033[m')
    elif computer == 2:
        print('Computador jogou Tesoura')
        print('EMPATE!!!!')
print('-=-=-=' * 20)