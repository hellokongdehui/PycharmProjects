# Author：D.H
# Place：哈工深
# Time：2021/7/27 11:23
# 练习5-9：处理没有用户的情形

users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')
else:
    print('We need to find some users!')