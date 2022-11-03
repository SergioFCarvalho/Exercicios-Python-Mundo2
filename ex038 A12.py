# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O  \033[1mprimeiro\033[m valor é MAIOR')
elif n2 > n1:
    print('O  \033[1msegundo\033[m valor é \033[1mMAIOR')
else:
    print('Os dois valores são \033[1mIGUAIS')
