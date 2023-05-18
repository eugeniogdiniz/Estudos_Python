alien_0 = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position':25, 'speed': 'medium'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

print("Original x position: " + str(alien_0['x_position']))

#Move o alienígena para direita
#Determina a distância que o alienígena deve se deslocar de 
#acordo com sua velocidade atual

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #este deve ser um alienígena muito rápido
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

del alien_0['points']
print(alien_0)