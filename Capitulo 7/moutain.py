responses = {}

#Define uma flag para indicar que a enquete está ativa
polling_active =True

while polling_active:
    #Pede o nome da pessoa e a resposta
    name = input("\nWhat is your name? ")
    response = input("Which moutain would you like to climb someday? ")
    #Armazena a resposta no dicionário
    responses[name] = response

    #Descobre se outra pessoa vai responder a enquete
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#A enquete foi concluída. Mostra os resultados
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

#O programa inicialmente define um dicionário vazio (responses) e cria
#uma flag (polling_active) para indicar que a enquete está ativa. Enquanto
#polling_active for True, Python executará o código que está no laço while.
#Nesse laço é solicitado ao usuário que entre com seu nome e uma
#montanha que gostaria de escalar u. Essa informação é armazenada no
#dicionário responses v, e uma pergunta é feita ao usuário para saber se ele
#quer que a enquete continue w. Se o usuário responder yes, o programa
#entrará no laço while novamente. Se responder no, a flag polling_active será
#definida com False, o laço while para de executar e o último bloco de
#código em x exibe o resultado da enquete.

