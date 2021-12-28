# Author：D.H
# Place：哈工深
# Time：2021/8/1 8:51
# 8.4 传递列表
def greet_users(names):
    """向列表中的每位用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)