linguagens = {
    'Eugenio': 'identação', 'Felipe': 'c++',
    'Marx': 'r', 'Lucas': 'Power Bi',
    'Luana': 'Julia', 'Raissa': 'Java',
    'Alex': 'linguagem M', 'Luiz': 'python',
    'Alessandra': 'r', 'Matheus': 'python',
}

#print("Palavras novas:")
#for palavra in set(linguagens.values()):
#    print(palavra.title())
#(print("\nPessoas na pesquisa:"))
#for name in linguagens.keys():
#    print(name.title())

for chave,valor in linguagens.items():
    print("\nA pessoa é a: " + chave.title() + ".")
    print("\tA linguagem escolhida é: " + valor.title() + ".")
