# Author：D.H
# Place：哈工深
# Time：2021/7/23 23:08
#2.3.2 在字符串中使用变量
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}" #f字符串，f是format（设置格式）的简写
print(full_name)

print(f'hello,{full_name.title()}!') #添加hello等，并用title（）设置格式

message=f"helo,{full_name}!" #用f字符串来创建消息，再将消息赋值给变量message
print(message)