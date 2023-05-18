#A abordagem descrita antes para gerar a lista squares usou três ou quatro
#linhas de código. Uma list comprehension (abrangência de lista) permite
#gerar essa mesma lista com apenas uma linha de código. Uma list
#comprehension combina o laço for e a criação de novos elementos em uma
#linha, e concatena cada novo elemento automaticamente. As list
#comprehensions nem sempre são apresentadas aos iniciantes, mas eu as
#incluí aqui porque é bem provável que você as veja assim que começar a
#analisar códigos de outras pessoas.
#O exemplo a seguir cria a mesma lista de quadrados perfeitos que vimos
#antes, porém utiliza uma list comprehension:

squares = [value **2 for value in range(1,11)]
print(squares)