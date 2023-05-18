for value in range(1,5):
    print(value)

#Nesse exemplo, range() exibe apenas os números de 1 a 4. Esse é outro
#resultado do comportamento deslocado de um que veremos com
#frequência nas linguagens de programação. A função range() faz Python
#começar a contar no primeiro valor que você lhe fornecer e parar quando
#atingir o segundo valor especificado. Como ele para nesse segundo valor, a
#saída não conterá o valor final, que seria 5, nesse caso.
#Para exibir os números de 1 a 5, você deve usar range(1,6):

for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)