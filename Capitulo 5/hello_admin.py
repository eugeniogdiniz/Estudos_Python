names = ['eugenio', 'lucas', 'admin']
if names:
    for name in names:
        if name.lower() == 'admin':
            print("Olá Admin, gostaria de ver um relatório de status?")
        else:
            print("Olá " + name.title() + ", obrigado por fazer login novamente.")
else:
    print("Precisamos de mais usuários!")
