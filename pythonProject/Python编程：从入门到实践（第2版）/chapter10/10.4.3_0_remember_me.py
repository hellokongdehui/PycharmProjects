# Author:D.辉
# Place：哈工深
# Time：2021/08/17 23:59
# 10.4.3 重构

import json

def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name?")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username.upper()}!")
    else:
        print(f"Welcome back, {username.upper()}!")


greet_user()
