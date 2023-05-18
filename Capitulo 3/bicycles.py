bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[0].upper())
print(bicycles[1])
print(bicycles[3])

#Python tem uma sintaxe especial para acessar o último elemento de uma
#lista. Ao solicitar o item no índice -1, Python sempre devolve 
#o último item da lista:

print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)