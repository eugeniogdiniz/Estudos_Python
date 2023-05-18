favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#Essa instrução for é como as outras instruções for, exceto que a função
#sorted() está em torno do método dictionary.keys(). Isso diz a Python para
#listar todas as chaves do dicionário e ordenar essa lista antes de percorrê-la
#com um laço.
