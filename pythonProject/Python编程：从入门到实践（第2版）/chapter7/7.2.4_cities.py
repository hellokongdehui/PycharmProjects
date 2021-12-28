# Author：D.H
# Place：哈工深
# Time：2021/7/30 7:51
# 7.2.4 使用break退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")