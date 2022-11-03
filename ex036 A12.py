# Ex Aprovando Empréstimo
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


print('\033[1m Programa para aprovação de empréstimo\033[m')
valor = float(input(' Valor da casa: R$ '))
salario = float(input('Qual seu salário: R$ '))
anos = int(input('Quantos anos de financiamento? '))
#meses = anos * 12 transformação de anos em meses. ou parcela = valor / (anos * 12)
parcelas = float(valor/anos)/12
x = (salario * 30)/100
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${parcelas:.2f}')
if parcelas > x:
    print('Empréstimo \033[31mNEGADO!')
else:
    print('Empréstimo pode ser \033[32mCONCEDIDO!')


