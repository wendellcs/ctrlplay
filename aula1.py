# ctrl + s -> Salvar as alterações do arquivo.
# ctrl + c -> Copiar
# ctrl + v -> Colar

# print() -> Mostra uma informação no terminal.

# str / String -> Texto / cadeia de caracteres
print('Primeira aula de Python')

# int -> Números inteiros
print(15)

# float -> Números com casas decimais
print(3.14)

# bool / Boolean -> Tipo lógico / Verdadeiro ou falso / True or False
print(True)

# type() -> Retorna o tipo de um dado

print(type(False))

# Operadores aritméticos

# * / - +

print((5 + 4) * 2)

# Operadores lógicos 

# >   <   ==     >=   <=   !=

print(5 > 2) # True
print(5 < 2) # False
print(5 == '5') # False
print('5' == '5 ') # False
print('5' == '5') # True
print('oi' != 'oi') # False
print(5 >= 5) # True
print(5 >= 6) # False
print(6 >= 5) # True
 
# and  or   not 

print(5 > 2 and 3 > 2) # True
print(5 > 2 and 3 < 2) # False

print(5 > 2 or 3 < 2) # True
print(5 > 2 or 3 > 2) # True

print(not(True)) # False
print(not(3 > 2)) # False
print(not(2 > 3)) # True

print(not((3 > 2 and 2 < 3) or 5 < 2))

# Variável

# Uma variável é um espaço na memória do computador
# Esse espaço pode guardar um valor
# Esse valor pode ser lido ou alterado sempre que necessário

# Definindo variáveis

# 1 - Nunca começar com um número ( Pode conter um número. Ex: nome1 )
# 2 - Não pode conter espaços ( primeiro_nome )
# 3 - Não pode conter simbolos 

# nome = 'Wendell'
# print(nome)

# 1 - Crie uma variável com o nome que faça sentido com a informação
# que será guardada nela.

idade = 22
cidade = 'Rio de Janeiro'
pais = 'Brasil'

# input() -> Entrada de dados

nome = input('Digite seu nome: ')
print('Seu nome é: ', nome)

# 2 - Pergunte a idade do usuário e retorne uma frase contendo a 
# idade dele.