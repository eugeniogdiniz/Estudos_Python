#O método sort() mostrado em u altera a ordem da lista de forma
#permanente. Os carros agora estão em ordem alfabética e não podemos
#mais retornar à ordem original.

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: ")
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)