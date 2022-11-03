#  Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerrará quando ele disser que quer mostrar 0 termos.
print('>>> Super Progressão Aritmética v3.0 <<<')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais_termos = 10
while mais_termos !=0:
    total += mais_termos
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais_termos = int(input('\nQuantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')