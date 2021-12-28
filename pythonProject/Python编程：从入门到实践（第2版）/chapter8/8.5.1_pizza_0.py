# Author：D.H
# Place：哈工深
# Time：2021/8/2 19:55
# 8.5.1 结合使用位置实参和任意数量实参

def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f'\nMaking a {size} pizza with the following toppings:')
    for topping in toppings:
        print(f"-{topping}")


make_pizza('12', 'peperoni')
make_pizza(21, 'mushrooms', 'green peppers', 'extra cheese')
