#  Faça um programa que leia um número qualquer e mostre o seu fatorial.
#  Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

# 1 usando módulo math

'''from math import factorial
numero = int(input('Digite um número para\ncalcular seu fatorial: '))
fatorial = factorial(numero)
print(f'O fatorial do número {numero} é {fatorial}')'''

#2 usando While

'''numero = int(input('Digite um número para\ncalcular seu fatorial:'))
contador = numero
resultado = 1
print(f'Calculando {numero}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x 'if contador > 1 else ' = ', end='')
    resultado *= contador
    contador -= 1
print(resultado)'''

#3 usando For

num = int(input('Digite um número para\ncalcular seu fatorial:'))
c = num
r = 1
print(f'Calculando {num}! = ', end='')
for c in range(num,0,-1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    r *= c
    c -= 1
print(r)