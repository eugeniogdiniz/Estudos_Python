def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

#Este é um loop infinito
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")