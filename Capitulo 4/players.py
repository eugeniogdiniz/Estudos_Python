players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3]) #todos os itens de 0 à 3
print(players[1:4]) #todos os itens de 1 à 4
print(players[:3]) #todos os itens até o 3
print(players[2:]) #todos os itens a partir do 2

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
