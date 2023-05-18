pizza = ['4 queijo', 'frango', 'calabresa']
friend_pizza = pizza[:]
friend_pizza.append('brocolis')
print('Minhas pizzas favoritas são: ')
for value in pizza:
    print(value)

print('\nAs pizzas favoritas do meu melhor amigo são:')
for value in friend_pizza:
    print(value)