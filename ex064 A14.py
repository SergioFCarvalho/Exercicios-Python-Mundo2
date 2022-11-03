# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print('~~' * 20)
print('---  \033[1;36;40mTratando vários valores v1.0\033[m ---')
print('~~' * 20)

# Forma alternativa como eu resolve
'''valor = cont = soma = 0
while valor !=999:
    valor =int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += valor
    if soma > 999:
        cont -= 1
        soma -= 999
print(f' Foram Digitados {cont} valores e a soma entre eles foi {soma}')'''

# Forma resolvida na aula do ex
valor = cont = soma = 0
valor =int(input('Digite um número [999 para parar]: '))
while valor != 999:
    soma += valor
    cont += 1
    valor = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} valores e a soma entre eles foi {soma}.')
