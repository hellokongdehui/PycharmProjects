# Author：D.H
# Place：哈工深
# Time：2021/7/25 18:04
# 练习4-12：使用多个循环
my_foods = ['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

print(f'my favorite foods are:{my_foods}')
print(f"\nmy friend's favorite foods are:{friend_foods}.")

for mf in my_foods[:]:
    print(mf.title())

for ff in friend_foods[:]:
    print(ff.title())