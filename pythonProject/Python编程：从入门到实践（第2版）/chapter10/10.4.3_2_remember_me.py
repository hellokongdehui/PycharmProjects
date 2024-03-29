# Author:D.辉
# Place：哈工深
# Time：2021/08/18 0:09
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


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.upper()}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.upper()}!")


greet_user()
