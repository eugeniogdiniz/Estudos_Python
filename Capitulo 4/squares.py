squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

#Começamos com uma lista vazia chamada squares em u. Em v, dizemos a
#Python para percorrer cada valor de 1 a 10 usando a função range(). No
#laço, o valor atual é elevado ao quadrado e armazenado na variável square
#em w. Em x, cada novo valor de square é concatenado à lista squares. Por
#fim, quando o laço acaba de executar, a lista de quadrados é exibida em y:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)