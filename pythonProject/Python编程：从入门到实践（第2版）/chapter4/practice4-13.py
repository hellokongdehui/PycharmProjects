# Author：D.H
# Place：哈工深
# Time：2021/7/25 21:11
# 练习4-13：自助餐
foods = ('jiangyouji', 'douchiya', 'shaoya', 'baiqieji', 'yanjuji')
for food in foods:
    print(food)

# foods[1]=211  TypeError: 'tuple' object does not support item assignment

print('---修改菜单---')
foods=('jiangyouji','douchiya','shaoya','白切鸡','盐焗鸡')
for food in foods:
    print(food)