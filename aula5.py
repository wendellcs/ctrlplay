# Estruturas de repetição ( Loops )

jogos = ['Resident Evil', 'Flappy Bird', 'The last of us', 'Jogo da velha', 'Untitled Goose Game', 'Roblox', 'Minecraft', 'Brawl Stars', 'Super Mario Bros', 'Sonic', 'Terraria', 'CS:2', 'Team Fortress 2', 'Half-Life', 'Drive beyond Horizon', 'CS:Source', 'DeadLock', "Garry's mod", 'Final Fantasy', 'Forza Horizon', 'Need For Speed']

numeros = list(range(0 , 100))

# For

# range() - Cria um intervalor entre valores escolhidos.

for i in range(len(jogos)):
    print(i + 1 , '-', jogos[i])

# 1 - Crie um loop que mostre uma contagem de 1 à 10.
# Dica: Use a função range().

# 2 - Crie uma lista com pelo menos 8 itens e mostre cada um 
# deles no terminal.

# Não usar: range(len(lista))

# 3 - Crie um loop de 0 à 20 e mostre no terminal apenas os números
# que forem maiores do que 10.

# for n in range(201):
#     if n == 100:
#         pass

# Loop while
x = 0
while True:
    if x == 100:
        break
    
    print(x)
    x+=1
