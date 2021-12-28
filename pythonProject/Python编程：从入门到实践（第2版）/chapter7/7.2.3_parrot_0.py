# Author：D.H
# Place：哈工深
# Time：2021/7/30 7:20
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += '\nEnter "quit" to end the program.'
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)