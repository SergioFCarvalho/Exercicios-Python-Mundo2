# Bases Numéricas
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número inteiro: '))
print('''\033[1mEscolha umas das bases para conversão \033[m
[1] para \033[1;32mBinário\033[m
[2] para \033[1;32mOctal\033[m
[3] para \033[1;32mHexadecimal\033[m''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print(f'{n} convertido para \033[1mBINÁRIO\033[m é {bin(n)[2:]}')
elif opçao == 2:
    print(f'{n} convertido para \033[1mOCTAL\033[m é {oct(n)[2:]}')
elif opçao == 3:
    print(f'{n} convertido para \033[1mHEXADECIMAL\033[m é {hex(n)[2:]}')
else:
    print('Opção inválida tente novamente!')