# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
número = int(input('Digite um número: '))
tot = 0
for c in range(1,número+1):
    if número % c ==0:
        print('\033[1;33m', end='')
        tot += 1
    else:
        print('\033[31m',end='')
    print(f' {c}', end=' ')
print(f'\n\033[mO número {número} foi divisível {tot} vezes.')
if tot ==2:
    print('O número escolhido É PRIMO!')
else:
    print(' O número escolhido NÃO É PRIMO!')
    