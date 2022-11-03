# O Curso de Python está de volta no seu Mundo 2 e
# vai falar sobre Estruturas de Controle da linguagem: if.. elif.. else, for e while.

# Aula 12 teste
nome = str(input('Qual seu nome? '))
if nome == 'Sérgio':
    nome.upper()
    print(f'Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jessi Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')










