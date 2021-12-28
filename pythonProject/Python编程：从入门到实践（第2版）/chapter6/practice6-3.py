# Author：D.H
# Place：哈工深
# Time：2021/7/27 21:00
# 练习6-3：词汇表
names = {
    '\t': '制表符',
    '\n': '换行符',
    'rstrip': '删除字符串末尾的空白',
    'lstrip': '删除字符串开头的空白',
    'strip': '删除字符串两边的空白',
    }
word = '\t'
print(f"\ t: {names[word]}")

word = '\n'
print(f"{word}\ n: {names[word]}")

word = 'rstrip'
print(f"{word}: {names[word]}")

word = 'lstrip'
print(f"{word}: {names[word]}")

word = 'strip'
print(f"{word}: {names[word]}")