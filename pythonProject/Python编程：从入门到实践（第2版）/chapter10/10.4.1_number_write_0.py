# Author:D.辉
# Place：哈工深
# Time：2021/08/17 23:16
# 10.4.1 使用json.dump()和json.load()

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
