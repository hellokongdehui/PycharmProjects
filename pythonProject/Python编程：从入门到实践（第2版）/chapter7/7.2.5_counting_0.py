# Author：D.H
# Place：哈工深
# Time：2021/7/30 8:02
# 7.2.5 在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)