# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior =0
totmenor =0
for pessoa in range(1,8):
    nasc = int(input(f'Em que ano nasceu a {pessoa}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >=18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Exixtem ao todo {totmaior} pessoas de maiores de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade')
