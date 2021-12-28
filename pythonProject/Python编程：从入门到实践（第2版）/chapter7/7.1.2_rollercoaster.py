# Author：D.H
# Place：哈工深
# Time：2021/7/29 23:34
# 使用int（）来获取数值输入
height = input('How tall are you, in inches?')
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")