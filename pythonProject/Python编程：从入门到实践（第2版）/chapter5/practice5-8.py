# Author：D.H
# Place：哈工深
# Time：2021/7/27 11:14
# 练习5-8:以特殊方式跟管理员打招呼
users = ['admin', 'bba', 'caa', 'dna', 'eco']
for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again.')