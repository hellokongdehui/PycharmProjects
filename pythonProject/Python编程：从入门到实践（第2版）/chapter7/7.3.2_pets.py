# Author：D.H
# Place：哈工深
# Time：2021/7/30 8:40
# 7.3.1 删除为特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)