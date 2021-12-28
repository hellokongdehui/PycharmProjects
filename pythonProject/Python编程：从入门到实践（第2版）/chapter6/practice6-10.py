# Author：D.H
# Place：哈工深
# Time：2021/7/29 14:52
# 练习6-10：喜欢的数2
favorite_numbers = {
    'jack': [12, 7],
    'jordon': [8, 9],
    'lisa': [99, 66],
    'tom': [88, 60],
    'lucy': [66, 33],
    }
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f" {number}")