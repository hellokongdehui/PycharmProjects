# Author:D.辉
# Place：哈工深
# Time：2021/08/16 20:58
# 10.1.3 逐行读取

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
