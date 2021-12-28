# Author:D.辉
# Place：哈工深
# Time：2021/08/17 22:09
# 10.3.5 处理FileNotFoundError异常

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry， the file {filename} does not exist.")
