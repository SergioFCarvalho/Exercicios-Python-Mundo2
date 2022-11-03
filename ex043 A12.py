# Índice de Massa Corporal
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

print('    Índice de Massa Corporal   ')
peso = float(input('Digite seu peso: (Kg)'))
altura = float(input('Digite sua altura: (m)'))
imc = peso/(altura**2)
print(f'O IMC dessa pessoa é {imc:.1f}')
if imc < 18.5:          #– IMC abaixo de 18,5: Abaixo do Peso
    print('Você está: ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:  #- Entre 18,5 e 25: Peso Ideal
    print('Parabéns, você está no PESO IDEAL!')
elif 25 <= imc < 30:    #– 25 até 30: Sobrepeso
    print('Você está em SOBREPESO!')
elif 30<= imc < 40:     #– 30 até 40: Obesidade
    print('Você está em OBESIDADE!')
elif imc >= 40:         #– Acima de 40: Obesidade Mórbida
    print('Você está em OBESIDADE MÓRBIDA!')
