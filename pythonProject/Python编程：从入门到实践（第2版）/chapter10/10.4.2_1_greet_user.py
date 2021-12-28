# Author:D.辉
# Place：哈工深
# Time：2021/08/17 23:39
# 10.4.2 保存和读取用户生成的数据

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)

print(f"Welcome back, {username.upper()}!")
