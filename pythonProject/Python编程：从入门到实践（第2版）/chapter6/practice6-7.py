# Author：D.H
# Place：哈工深
# Time：2021/7/29 14:16
# 练习6-7：人们
people = []

person = {
    'first_name': 'kong',
    'last_name': 'dehui',
    'age': 25,
    'city': 'shenzhen',
    }
people.append(person)

person = {
    'first_name': 'lemmy',
    'last_name': 'matthes',
    'age': 2,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 11,
    'city': 'guangzhou',
    }

print(people)

people.append(person)
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()} "
    age = person['age']
    city = person['city'].title()
    print(f"{name}, of {city}, is {age} years old.")