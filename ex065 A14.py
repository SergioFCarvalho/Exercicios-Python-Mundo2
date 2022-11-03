#  Crie um programa que leia vários números inteiros pelo teclado.
#  No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('>> Maior e Menor valores <<')
soma = quantidade = media = maior = menor = valor = 0
pergunta = 'S'
while pergunta == 'S':
    valor = int(input('Digite um número: '))
    pergunta = str(input('Quer continuar \033[1m[S/N]?\033[m')).upper().strip()[0]
    soma += valor
    quantidade += 1
    if quantidade == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
media = soma/quantidade
print(f'Você digitou {quantidade} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor {menor}')
