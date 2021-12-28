# Author:D.辉
# Place：哈工深
# Time：2021/08/14 23:21
# 10.1.1 读取整个文件

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
