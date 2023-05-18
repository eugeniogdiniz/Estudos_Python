#Também podemos usar o método remove() para trabalhar com um valor
#que está sendo removido de uma lista. Vamos remover o valor 'ducati' e
#exibir um motivo para removê-lo da lista:

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#O método remove() apaga apenas a primeira ocorrência do valor que você
#especificar. Se houver a possibilidade de o valor aparecer mais de uma vez na
#lista, será necessário usar um laço para determinar se todas as ocorrências desse
#valor foram removidas.

