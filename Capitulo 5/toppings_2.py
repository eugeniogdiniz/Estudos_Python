requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Dessa vez, começamos com uma lista vazia de ingredientes solicitados em
#u. Em vez de passar diretamente para um laço for, fazemos uma verificação
#rápida em v. Quando o nome de uma lista é usado em uma instrução if,
#Python devolve True se a lista contiver pelo menos um item; uma lista vazia
#é avaliada como False. Se requested_toppings passar no teste condicional,
#executamos o mesmo laço for do exemplo anterior.
#Se a lista não estiver vazia, a saída mostrará cada ingrediente solicitado
#adicionado à pizza.