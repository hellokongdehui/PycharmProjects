# Author:D.辉
# Place：哈工深
# Time：2021/08/17 23:26
# 10.4.2 保存和读取用户生成的数据

import json

username = input("What is your name?")

filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f)

print(f"We'll remember you when you come back, {username.upper()}!")
