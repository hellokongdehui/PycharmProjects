# Author:D.辉
# Place：哈工深
# Time：2021/08/17 23:05
# 10.4.1 使用json.dump()和json.load()

import json

numbers = [2, 3, 5, 7, 11]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
