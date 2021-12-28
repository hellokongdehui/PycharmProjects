# Author：D.H
# Place：哈工深
# Time：2021/7/29 23:24
# 编写清晰的程序
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"
print(prompt)

name = input(prompt)
print(f"\nHello, {name}!")