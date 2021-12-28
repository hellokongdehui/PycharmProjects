# Author:D.辉
# Place：哈工深
# Time：2021/08/17 20:06
# 10.2.2 写入多行

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write("I love creating new games.\n")

