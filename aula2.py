# Resumo da aula 1

# Tipos primitivos

# bool / Boolean -> Tipo lógico / True or False
verdadeiro = True
falso = False

# str / String -> Cadeias de caracteres / Textos
texto = 'Wendell é professor de programação'

# float -> Números com casas decimais
pi = 3.14

# int -> Números inteiros
numero = 15

# Operadores aritmeticos

# * / + - ------- % //

print(9 % 2)
print(9 // 2)

# print() -> Usada para mostrar alguma informação no terminal.

# Operadores lógicos

# > - < - == - >= - <= - !=

print(5 == 5)
print(6 != 6)

# and - or - not

print(5 > 2 and 3 > 4)

print(5 > 2 or 3 > 5)

print(not(3 > 5))

# Variáveis 

# É um espaço na memória do computador que armazena um valor, esse 
# valor pode ser lido ou alterado sempre que necessário.

idade = 18

print(idade)

idade = 20

print(idade)

# Regras para criar uma variável

# 1 - Não começar o nome com um número
# 2 - Não pode conter simbolos 
# 3 - Não pode conter espaço

segundo_nome = 'Silva'

# input() -> Entrada de dados do usuário

# nome = input('Insira seu nome: ')
# print('Seu nome é:', nome)

# 1 - Exercicio 
# Crie um input que receba a idade do usuário e depois retorne a idade
# junto de uma frase.




# Aula 2 

# Manipulando strings

# Concatenação

parte_1 = 'Daniel'
parte_2 = ' Video Maker'
frase = parte_1 + parte_2 + '!'

print(frase)


# Indexação 
palavra = 'Melancia'

print(palavra[0])
print(palavra[0 : 3])
print(palavra[2 : 5])
print(palavra[-1])
print(palavra[2:])
print(palavra[:5])

# Funções de string

# len() -> lenght -> Comprimento de uma string
print(len(palavra))

# find() -> Retorna a posição de um elemento no texto
print(palavra.find('a'))

# count() -> Conta a quantidade de aparições de um elemento escolhido
print(palavra.count('a'))

# str() -> Converte um valor para string
# type() -> Mostra o tipo de um elemento

print(type(str(15)))

# Exercicio

# Crie um programa que, dada uma string com uma frase informada 
# pelo usuário (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

texto = input('Digite algo: ')
print(palavra.count('a'))
# count() -- input('Digite uma frase: ')