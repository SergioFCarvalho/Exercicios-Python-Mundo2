# Analisando Triângulos v2.0 , acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes
print('*' * 40)
print('  \033[1mAnalisador de Triângulos v2.0\033[m  ')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print('Os segmentos acima podem forma um triângulo \033[1mEQUILÁTERO')
    elif a != b != c != a:
        print('Os segmentos acima podem forma um triângulo \033[1mESCALENO')
    else:
        print('Os segmentos acima podem forma um triângulo \033[1mISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMA um triângulo !')
