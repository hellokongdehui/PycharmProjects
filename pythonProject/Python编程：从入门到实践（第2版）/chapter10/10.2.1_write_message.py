# Author:D.辉
# Place：哈工深
# Time：2021/08/17 19:59
# 10.2.1 写入空文件

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
