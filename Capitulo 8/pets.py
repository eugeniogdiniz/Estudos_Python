def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')

#A definição mostra que essa função precisa de um tipo de animal e de seu
#nome u. Quando chamamos describe_pet(), devemos fornecer o tipo do
#animal e um nome, nessa ordem. Por exemplo, na chamada da função, o
#argumento 'hamster' é armazenado no parâmetro animal_type e o
#argumento 'harry' é armazenado no parâmetro pet_name v.