# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
from time import sleep
opcao = 0
valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))
while opcao != 5:
    opcao = int(input('''   \033[1;32m[ 1 ]\033[m somar \033[1;33m[ 2 ]\033[m multiplicar \033[1;34m[ 3 ]\033[m maior 
    \033[1m[ 4 ]\033[m novos números \033[;1m[ 5 ]\033[m sair do programa
    >>>> Qual sua opção? '''))
    print('-=' * 20)
    if opcao == 1:
        soma = valor_1 + valor_2
        print(f'A soma entre {valor_1} e {valor_2} é {soma}')
    elif opcao == 2:
        multiplicar = valor_1 * valor_2
        print(f'O resultado entre {valor_1} x {valor_2} é {multiplicar}')
    elif opcao == 3:
        if valor_1 > valor_2:
            maior = valor_1
        else:
            maior = valor_2
        print(f'Entre {valor_1} e {valor_2} o maior é {maior}')
    elif opcao == 4:
        print('Informe novos números')
        valor_1 = int(input('Primeiro valor: '))
        valor_2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
        print('-=' * 20)
        print('\033[1;92;40mFim do programa! Volte sempre!\033[m')
        break
    else:
        print('\033[1;91mOpção inválida\033[m.....')
    print('-=' * 20)