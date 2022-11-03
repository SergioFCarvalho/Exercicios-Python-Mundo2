# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
média_idade = 0
maior_idade_homem = 0
nome_homem_velho = ''
total_mulher = 0
for pessoa in range(1,5):
    print(f'----{pessoa}ª pessoa-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher += 1
print('  ')
média_idade = soma_idade/4
print(f'A média de idade do grupo é de {média_idade:.1f} anos.')
print(f'O homem mais velho se chama {nome_homem_velho} e tem {maior_idade_homem} anos.')
print(f'Ao todo são {total_mulher} mulher(es) com menos de 20 anos.')