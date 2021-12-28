# Author：D.H
# Place：哈工深
# Time：2021/7/30 15:37
# 8.2.2 关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')
