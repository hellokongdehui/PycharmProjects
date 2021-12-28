# Author：D.H
# Place：哈工深
# Time：2021/7/30 8:08
# 7.2.6 避免无限循环
x = 1
while x <= 5:
    print(x)
    x += 1

print('================')
x = 1
while x <= 5:
    x += 1
    print(x)
