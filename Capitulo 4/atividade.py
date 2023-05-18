#conte até vinte
for value in range(1,21):
    print(value)

#crie uma lista de 1 até 1000K
list_1 = [value + 1 for value in range(0,100000)]
print(min(list_1))
print(max(list_1))
print(sum(list_1))

#numeros impares
for value in range(1,21,2):
    print(value)

#tres
list_2 = [value * 3 for value in range(1,11)]
print(list_2)

#cubos
list_3 = [value ** 3 for value in range(1,11)]
print(list_3)