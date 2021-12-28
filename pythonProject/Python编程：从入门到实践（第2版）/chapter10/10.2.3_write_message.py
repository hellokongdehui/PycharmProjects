# Author:D.辉
# Place：哈工深
# Time：2021/08/17 20:14
# 10.2.3 附加到文件

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
