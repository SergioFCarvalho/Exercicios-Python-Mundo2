 # Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

# nome = str(input('Digite nome do aluno: ')).strip()
not1 = float(input('Digite sua primeira nota: '))
not2 = float(input('Digite sua segunda nota: '))
media = (not1 + not2)/2
if media >= 7:
    print(f'Sua média é {media:.1f}, parabéns você foi \033[32mAPROVADO!')
elif media < 5:
    print(f'Sua média foi {media:1f}, infelizmente você esta \033[31mREPROVADO!')
elif media >= 5 and  media <= 6.9:
    print(f'Sua média foi {media:.1f}, você está na \033[1;33mRECUPERAÇÃO!')
