# Author：D.H
# Place：哈工深
# Time：2021/7/30 7:05
# 7.2.2让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += '\nEnter "quit" to end the program.'
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)