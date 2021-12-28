# Author：D.H
# Place：哈工深
# Time：2021/7/31 7:04
# 8.2.3 默认值
def describe_pet(pet_name, animal_type='dog'):  # 默认值要放在后面
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# 由于添加了默认值，任何时候都需要有pet_name实参
describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet('harry', 'hamster')
