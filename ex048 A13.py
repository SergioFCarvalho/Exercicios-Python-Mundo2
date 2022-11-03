# Faça um programa que calcule a soma entre todos os números que são múltiplos
# de 3 e que se encontram no intervalo de 1 até 500.
s = 0
c = 0
for num in range(3, 501, 6):
    c = c + 1
    s = s + num
print(f'A soma de todos os {c} valores solicitados é {s}')
