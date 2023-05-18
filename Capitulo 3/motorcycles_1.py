motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'ducati')
print(motorcycles)

#Nesse exemplo, o código em u insere o valor 'ducati' no início da lista. O
#método insert() abre um espaço na posição 0 e armazena o valor 'ducati'
#nesse local.

del motorcycles[3]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motocycle = motorcycles.pop()
print(motorcycles)
print(popped_motocycle)

#Como esse método pop() poderia ser útil? Suponha que as motocicletas
#da lista estejam armazenadas em ordem cronológica, de acordo com a
#época em que fomos seus proprietários. Se for esse o caso, podemos usar o
#método pop() para exibir uma afirmação sobre a última motocicleta que
#compramos

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + '.')

first_owner = motorcycles.pop(0)
print('The first motorcycle I owned was a' + first_owner.title() + '.')

#Também podemos usar o método remove() para trabalhar com um valor
#que está sendo removido de uma lista.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)