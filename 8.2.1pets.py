def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('dog','harry')
describe_pet('hamter','willie')
describe_pet('hamter','dog')
describe_pet(pet_name='harry',animal_type='hamster')