# Author：D.H
# Place：哈工深
# Time：2021/7/29 14:28
# 练习6-8：宠物
# 创建一个用于存储宠物的空列表中
pets = []

# 定义各个宠物并将其存储到列表中
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': '43',
    'eats': 'bugs',
    }
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
    }
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
    }
pets.append(pet)

# 显示每个宠物发信息
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value, in pet.items():
        print(f"\t{key}: {value}")