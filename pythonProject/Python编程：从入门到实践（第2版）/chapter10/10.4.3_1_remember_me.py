# Author:D.辉
# Place：哈工深
# Time：2021/08/18 0:03
# 10.4.3 重构

import json


def get_stored_username():
    """如果存储了用户名，就获取它。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.upper()}!")
    else:
        username = input("What is your name?")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username.upper()}!")


greet_user()
