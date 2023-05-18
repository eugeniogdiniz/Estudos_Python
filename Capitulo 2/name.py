name = "aDA Lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#.title() faz com que cada palavra da string comece com uma maiuscula
#.upper() faz com que todas as palavras apareçam como maiusculas
#.lower() faz com que todas as palavras apareçam como minusculas

first_name = input("Digite seu nome:")
last_name = input("Digite seu sobrenome:")
full_name = first_name.title() + " " + last_name.title()
print(full_name)