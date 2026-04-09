# Estrutura de condição

# Vc só vai sair se lavar a louça

# Operadores lógicos

# > - Maior que
# < - Menor que
# == - Igual a
# != - Diferente de
# >= - Maior ou igual a
# <= - Menor ou igual a

# and - E - Retorna verdadeiro se ambos os lados forem verdadeiros
# or - Ou - Retorna verdadeiro quando pelo menos um lado for verdadeiro
# not() - Não - Inverte o valor

# Estrutura

# if condição:
    # Código

nome = 'Julia'
nome2 = 'Gabriela'

# input()

# palavra = input('Digite uma palavra qualquer: ')

# print('A palavra digitada foi: ' + palavra)
# if nome == nome2:
#     print(nome)
# else:
#     print(nome2)

# 1 - Crie um programa que pergunte a idade de um usuário
# Se ele for maior de idade, retorne um texto dizendo que ele é maior
# se n retorne um texto dizendo que ele é menor de idade.

idade = int(input('Insira sua idade: '))

if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')

# 2 - Peça ao usuário um número e informe se ele é 
# positivo, negativo ou 0. 
# OBS: Use o int() para converter o valor do input()

# if condição 1:
#     # código
# elif condição 2:
#     # código
# else:
#     # Código

# DESAFIO
# 3 - Peça dois números ao usuário e diga qual deles é o maior
