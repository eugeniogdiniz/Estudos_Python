def build_person(first_name, last_name):
    """Devolve um dicionário com informações sobre uma pessoa"""
    person = {'first': first_name, 'last': last_name}
    return  person

musician = build_person('jimi', 'hendrix')
print(musician)