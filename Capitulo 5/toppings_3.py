available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

#Em u definimos uma lista de ingredientes disponíveis nessa pizzaria.
#Observe que essa informação poderia ser uma tupla se a pizzaria tiver uma
#seleção estável de ingredientes. Em v criamos uma lista de ingredientes
#solicitados por um cliente. Observe a solicitação incomum, 'french fries'
#(batatas fritas). Em w percorremos a lista de ingredientes solicitados em
#um laço. Nesse laço, inicialmente verificamos se cada ingrediente solicitado
#está na lista de ingredientes disponíveis x. Se estiver, adicionamos esse
#ingrediente na pizza. Se o ingrediente solicitado não estiver na lista de
#ingredientes disponíveis, o bloco else será executado y. Esse bloco exibe
#uma mensagem informando ao usuário quais ingredientes não estão
#disponíveis.