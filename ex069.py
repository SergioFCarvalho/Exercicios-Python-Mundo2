# Análise de dados do grupo
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
'''
A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

print('=' * 20)
print('CADASTRE UMA PESSOA')
print('=' * 20)

total_idade18 = total_homens = total_mulher = 0
while True:
    idade = int(input('Idade: '))
    while idade < 1 or idade > 100:
        idade = int(input('Idade: '))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input('Sexo: \033[1;92m[M/F]\033[m ')).upper().strip()[0]
    print('-' * 20)
    if idade >= 18:
        total_idade18 += 1
    if sexo == 'M':
        total_homens += 1
    if idade < 20 and sexo == 'F':
        total_mulher += 1
    resp = " "
    while resp not in "SN":
        resp = str(input('Quer continuar? \033[1;92m[S/N]\033[m ')).upper().strip()[0]
    if resp == "N":
        break
print(f'Total de pessoas maiores de 18 anos: {total_idade18}')
print(f'Ao todo temos {total_homens} homen(s) cadastrados.')
print(f'E temos {total_mulher} mulher(s) com menos de 20 anos')


