# Author：D.H
# Place：哈工深
# Time：2021/7/25 17:49
#练习4-11：你的披萨，我的披萨
my_pizzas=['玛格丽特披萨','至尊披萨','鸡蛋香肠披萨','pizaa5','pizza6']
friend_pizzas=my_pizzas[:]
my_pizzas.append('pizza7')
friend_pizzas.append('pizza8')
print('My favorite pizzas are:')
for my in my_pizzas:
    print(my)
print(my_pizzas)
print("My friend's favorite pizzas are:")
for friend in friend_pizzas:
    print([friend])
print(friend_pizzas)
