# Author:D.辉
# Place：哈工深
# Time：2021/08/17 22:45
# 10.3.8 静默失败

def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        # 计算该文件大致包含多少个单词。
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
