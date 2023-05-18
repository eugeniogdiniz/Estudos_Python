requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping.lower() == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping.title() + ".")

print("\nFinished making your pizza!\n")

#Dessa vez verificamos cada item solicitado antes de adicioná-lo à pizza. O
#código em u verifica se a pessoa pediu pimentões verdes. Em caso
#afirmativo, exibimos uma mensagem informando por que ela não pode ter
#pimentões verdes. O bloco else em v garante que todos os demais
#ingredientes serão adicionados à pizza.

