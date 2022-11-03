# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print('      \033[1m Você deve se alistar? \033[m       ')
print('''Qual seu sexo?
[1] Masculino
[2] Feminino''')

opc = int(input('Escolha uma opção: '))
ano = int(input('Qual ano você nasceu: '))
hoje = date.today().year
idade = hoje - ano
print('     ')

print(f'Quem nasceu em {ano} tem {idade} anos em {hoje}.')
if idade > 18 and opc == 1:
    print(f'Você já deveria ter se alistado há {idade - 18} ano(s)')
    print(f'Seu alistamento foi em {ano + 18}.')
elif idade < 18 and opc == 1:
    print(f'Ainda faltam {18 - idade} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {ano + 18}.')
elif idade == 18 and opc == 1:
    print(f'Você tem {idade} anos deve se alistar imediatamente!')


if opc == 2:
    print('Você não é obrigada a se alistar')
elif opc > 2:
    print('Opção errada')
