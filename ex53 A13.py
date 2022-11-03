# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
# O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = juntos[::-1]
'''for letra in range(len(juntos) -1, -1, -1):
    inverso += juntos[letra]'''
print(f'O inverso de {juntos} é {inverso}')
if inverso == juntos:
    print('Temos um Palíndromo!')
else:
    print('Não é Palíndromo!')