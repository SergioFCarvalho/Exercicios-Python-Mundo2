# Jogo do Par ou Ímpar
from random import randint
print('*' * 15)
print('\033[1;100m PAR OU ÍMPAR \033[m')
print('*' * 15)

vitoria = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    pergunta = ' '
    while pergunta not in 'PI':
        pergunta = str(input('Par ou Ímpar: [P/I] ')).upper().strip()[0]
    print('--' * 25)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(' É PAR' if total % 2 == 0 else ' É ÍMPAR')
    print('--' * 25)
    if pergunta == 'P':
        if total % 2 == 0:
            print('\033[1;32mVocê Ganhou!!!\033[m')
            vitoria += 1
        else:
            print('\033[1;91mVocê Perdeu!!!\033[m')
            break
    elif pergunta == 'I':
        if total % 2 == 1:
            print('\033[1;32mVocê Ganhou!!!\033[m')
            vitoria += 1
        else:
            print('\033[1;91mVocê Perdeu!!!\033[m')
            break
    print('Vamos Jogar novamente.....')
print(f'GAME OVER!! Você venceu {vitoria} vezes.')