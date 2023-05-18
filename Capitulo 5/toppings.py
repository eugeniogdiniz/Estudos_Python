requested_topping = ['mushrooms', 'extra chesse']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra chesse' in requested_topping:
    print("Adding extra chesse.")
print("\nFinished making your pizza!")

#Começamos em u com uma lista contendo os ingredientes solicitados. A
#instrução if em v verifica se a pessoa pediu cogumelos ('mushrooms') em
#sua pizza. Em caso afirmativo, uma mensagem será exibida para confirmar
#esse ingrediente. O teste para pepperoni em w corresponde a outra
#instrução if simples, e não a uma instrução elif ou else, portanto esse
#teste é executado independentemente de o teste anterior ter passado ou
#não. O código em x verifica se queijo extra ('extra cheese') foi pedido, não
#importando o resultado dos dois primeiros testes. Esses três testes
#independentes são realizados sempre que o programa é executado.