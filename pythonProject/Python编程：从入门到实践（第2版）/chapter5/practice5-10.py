# Author：D.H
# Place：哈工深
# Time：2021/7/27 16:14
# 练习5-10：检查用户名
current_users = ['admin', 'BBA', 'caa', 'dna', 'eco']
new_users = ['honda', 'bba', 'CAA', 'audi', 'toyota']
current_users_lower = [user.lower() for user in current_users]
for user in new_users:
    if user.lower() in current_users_lower:
        print(f'{user} has been used, please try again!')
    else:
        print(f'{user} has not been used, you can use it!')
