# Author：D.H
# Place：哈工深
# Time：2021/8/2 19:36
# 8.5 传递任意数量的实参

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 遍历列表


def make_pizza(*toppings1):
    """概述要制作的披萨"""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings1:
        print(f"-{topping}")


make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
