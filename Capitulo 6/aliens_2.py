#Cria uma lista vazia para armazenas alienígenas

aliens = []

#cria 30 alienígenas verdes

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Mostra os 5 primeiros alienígenas

for alien in aliens[:5]:
    print(alien)
print("...")

#Mostra quantos alienígenas foram criados
print("Total number of aliens: " + str(len(aliens)))