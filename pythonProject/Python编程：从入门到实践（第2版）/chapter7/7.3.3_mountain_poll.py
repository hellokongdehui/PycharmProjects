# Author：D.H
# Place：哈工深
# Time：2021/7/30 8:47
# 7.3.3 使用用户输入来填充字典
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("\nWhich mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False

print('\n---Poll Results---')
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")