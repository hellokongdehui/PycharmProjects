# decoding=utf-8
# Author:D.辉
# Place：哈工深
# Time：2022/01/02 21:24
# 3.3 组织列表

cars = ['bwm', 'toyota', 'honda', 'audi', 'tesla']

# cars.sorted()  # 方式不对
# print(cars)  # AttributeError: 'list' object has no attribute 'sorted'

print(sorted(cars))  # 临时排序
print(cars)  # 恢复原样

# sort1 = cars.sort()  # 行不通
# print(sort1)  # None

cars.sort()  # 永久排序
print(cars)

cars.reverse()  # 倒着打印
print(cars)

len1 = len(cars)  # 统计长度 方式1
print(len1)
print(len(cars))  # 统计长度 方式2
