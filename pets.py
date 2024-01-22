def describe_per(animal_type, pet_name):
    """ 显示宠物的信息 """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_per('name', 'harry')
describe_per('dog', 'willie')

describe_per(animal_type='hamster', pet_name='harry')


def describe_pet(pet_name, pet_type='dog'):
    """ 显示宠物的信息 """
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')

describe_pet('willie')
