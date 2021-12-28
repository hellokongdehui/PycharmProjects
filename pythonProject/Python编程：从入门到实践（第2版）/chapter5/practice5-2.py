# Author：D.H
# Place：哈工深
# Time：2021/7/26 21:40
# 练习5-2：更多条件测试
print('检查两个字符串相等和不等：')
car = 'bmw'
if car == 'bmw':
    print("True")

car = 'audi'
if car != 'bmw':
    print("True")

print('使用方法lower()的测试：')
car = 'Audi'
if car.lower() == 'audi':
    print(car.lower())

print('涉及相等、不等、大于、小于、大于等于和小于等于的数值测试：')
age = 18
if age == 18:
    print('等于')

age1 = 18
if age1 != 19:
    print('不等于')

age2 = 19
if age2 > 18:
    print('大于')

age2 = 19
if age2 < 20:
    print('小于')

age2 = 19
if age2 >= 18:
    print('大于等于')

age2 = 19
if age2 <= 20:
    print('小于等于')

print('使用关键字and和or的测试：')
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print('age_0 >= 21 and age_1 >= 21:True')
else:
    print('age_0 >= 21 and age_1 >= 21:False')

age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print('age_0 >= 21 or age_1 >= 21: True')
else:
    print('age_0 >= 21 or age_1 >= 21:False')

print('测试特定的值否包含在列表中；')
requested_toppings = ['mushroom', 'onions', 'apple pipe']
if 'mushroom' in requested_toppings:
    print('yes!True!mushroom in the list!')
else:
    print('no!False!')

print('测试特定的值是否未包含在列表中；')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f'{user.title()},you can post a response if you wish.')
else:
    print(f'{user.title()},sorry,you can not post a response!')