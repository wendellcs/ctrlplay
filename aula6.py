
# Tuplas
dias_da_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
# Não posso adicionar ou remover valores.

# dias_da_semana.append('Teste')
# dias_da_semana.pop()
print(len(dias_da_semana))

# Sets() - Não aceita valores duplicados

numeros_unicos = set() 

for i in range(5):
    numeros_unicos.add(i)

# numeros_unicos.remove(2)

# [] - Listas
# () - Tuplas
# {} - Set

# Dicionário ( Estrutura que armazena uma chave e um valor )

carro = {
    'cores': ['preto', 'branco', 'vermelho'],
    'rodas': 4,
    'escapamento': 3,
    'motor': 'V12',
    'marca': 'BMW',
    'ano': 1970,
    'velocidade_maxima': '400km/h'
} 

# Atualizando o valor a partir de uma chave
# carro['cor'] = 'branco'
# Adicionando um novo item no dicionário.
carro['portas'] = 2

# carro.keys() - Pega as chaves do dicionário
# carro.values() - Pega os valores do dicionário
# carro.items() - Pega todos os itens do dicionário
print(carro.items())

# Adicione dois valores ao dicionário
# Atualize dois valores do dicionário

# print(carro)

# Matrizes

# Dada a lista (1,3,2,3,4,5,1,5,7,6,8,3,4), crie uma segunda lista apenas com os 
# itens na mesma ordem, mas sem repetição.