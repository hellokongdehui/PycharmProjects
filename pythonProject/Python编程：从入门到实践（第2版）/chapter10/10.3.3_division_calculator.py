# Author:D.辉
# Place：哈工深
# Time：2021/08/17 20:28
# 10.3.3 使用异常避免崩溃

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\n First number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
