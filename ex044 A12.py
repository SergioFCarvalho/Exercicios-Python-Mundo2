# Gerenciador de Pagamentos
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento

print('\033[1;31;107m=================== LOJAS TABAJARA ====================\033[m')
print('   ')
preço = float(input('Preço das compras: R$'))
print('''  FORMA DE PAGAMENTO
 [ 1 ]à vista dinheiro/cheque
 [ 2 ]à vista no cartão
 [ 3 ] em até 2x no cartão
 [ 4 ]3x ou mais no cartão''')
opc =int(input('Qual será a opção? '))

if opc == 1:            #à vista dinheiro/cheque: 10% de desconto
    p1 = preço - (preço * 10 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${p1:.2f} no final.')
elif opc == 2:          # à vista no cartão: 5% de desconto
    p1 = preço - (preço * 5 /100)
    print(f'Sua compra de R${preço:.2f} vai custar R${p1:.2f} no final.')
elif opc == 3:          # em até 2x no cartão: preço formal
    p1 = preço/2
    print(f'Sua compra de R${preço:.2f} em 2x no cartão vai custar {p1:.2f} no final.')
elif opc == 4:          # 3x ou mais no cartão: 20% de juros
    parc = int(input('Quantas parcelas? '))
    pt = preço + (preço * 20)/100
    p1 = pt / parc
    print(f'''Sua compra será parcelada {parc}x de R${p1:.2f} com juros
Sua compra de R${preço:.2f} vai custar R${pt:.2f} no final.''')
else:
    print('\033[31m OPÇÃO INVÁLIDA DE PAGAMENTO, tente novamente!!!')