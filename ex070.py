# Estatísticas em produtos               -> refazer de forma diferente
"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

print('\033[1m_\033[m' * 30)
print('   \n      \033[1;92mLOJA LEVE MENOS\033[m    ')
print('\033[1m_\033[1m' * 30)

soma = quantidade = menor = contador = 0
barato = ' '
while True:
    nome_produto = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$'))
    soma += valor
    contador += 1
    if valor > 1000:
        quantidade += 1
    if contador == 1 or valor < menor:
        menor = valor
        barato = nome_produto
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        break
print('-'* 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {quantidade} produto(s) que custam mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
