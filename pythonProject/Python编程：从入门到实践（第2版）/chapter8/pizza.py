# Author：D.H
# Place：哈工深
# Time：2021/8/3 8:17
# 8.6.1 导入整个模块
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f'{topping}')
