# Tabuada v3.0
"""
 Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo.
"""

print('~' * 20)
print('     Tabuada v3.0')
print('~' * 20)

while True:
    numero = int(input('Tabuada de qual valor: '))
    print('-' * 20)
    if numero < 0:
        break
    for y in range(1, 11):
        print(f'{numero} x {y} = {numero*y} ')
    print('-' * 20)
print('Programa tabuada encerrado.')


