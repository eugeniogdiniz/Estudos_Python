#Cria uma lista vazia para armazenas alienígenas

aliens = []

#cria 30 alienígenas verdes

for alien_number in range(30):
    new_alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
    new_alien_1 = {'color': 'red', 'points': 15, 'speed': 'speed'}
    new_alien_2 = {'color': 'yellow', 'points': 10, 'speed': 'slow'}
    aliens.append(new_alien_0)
    aliens.append(new_alien_1)
    aliens.append(new_alien_2)

#Mostra os 5 primeiros alienígenas

for alien in aliens[:3]:
    print(alien)
print("...")

#Mostra quantos alienígenas foram criados
print("Total number of aliens: " + str(len(aliens)))

#Esse exemplo começa com uma lista vazia para armazenar todos os
#alienígenas que serão criados. Em u range() devolve um conjunto de
#números, que simplesmente diz a Python quantas vezes queremos que o
#laço se repita. A cada vez que o laço é executado, criamos um novo
#alienígena v e concatenamos cada novo alienígena à lista aliens w.

