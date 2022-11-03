#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
print('>>>>  \033[1;30;103mSequência de Fibonacci v1.0\033[m <<<<')
numero_termos = int(input('Quantos termos você quer mostrar? '))
primeiro = 0
segundo = 1
cont = 3
print(f'{primeiro} → {segundo} → ', end='')
while cont <= numero_termos:
    terceiro = primeiro + segundo
    print(f' {terceiro} →', end='')
    primeiro = segundo
    segundo = terceiro
    cont += 1
print('fim')

