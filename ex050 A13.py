# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for w in range(1, 7):
    n = int(input(f'Digite {w} valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A soma dos valores pares é {soma}.')
print(f'Você informou {cont} valor(es) par(es).')