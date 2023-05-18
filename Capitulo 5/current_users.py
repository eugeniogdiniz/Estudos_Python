current_users = ['eugenio', 'felipe', 'joão', 'lucas', 'marx']
new_users = ['eugenio', 'carol', 'bernardes', 'gabriela', 'marx']

for user in new_users:
    if user in current_users:
        print("Nome do usuário (" + user.title() + ") já cadastrado!")
    else:
        print("Seja bem vindo " + user.title() + ".")
