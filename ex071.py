# Simulador de Caixa Eletrônico
"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

"""

print('<==>' * 5)
print('\033[1m    BANCO PPE \033[m ')
print('<==>' * 5)

# Minha solução,com mudanças.. nota de 100 e nota de 5, retirada da nota de 1 real

saque = int(input('Qual valor você quer sacar? R$'))

if saque >= 0:
    ced100 = saque // 100
    if ced100 != 0:
        print(f'Total de {ced100} cédulas de R$100')
    saque = saque - (ced100 * 100)
    ced50 = saque // 50
    if ced50 != 0:
        print(f'Total de {ced50} cédulas de R$50')
    saque = saque - (ced50 * 50)
    ced20 = saque // 20
    if ced20 != 0:
        print(f'Total de {ced20} cédulas de R$20')
    saque = saque - (ced20 * 20)
    ced10 = saque // 10
    if ced10 != 0:
        print(f'Total de {ced10} cédulas de R$10')
    saque = saque - (ced10 * 10)
    ced5 = saque // 5
    if ced5 != 0:
        print(f'Total de {ced5} cédulas de R$5')

""" 
# Solução baseada no professor fiz mudanças ....

valor = int(input('Qual valor do saque? R$'))
total = valor
total_cedulas = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'O total de {total_cedulas} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        total_cedulas = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco xyz')
"""
