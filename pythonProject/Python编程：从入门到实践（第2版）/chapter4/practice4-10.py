# Author：D.H
# Place：哈工深
# Time：2021/7/25 17:39
#练习 4-10:切片
pizzas=['玛格丽特披萨','至尊披萨','鸡蛋香肠披萨','pizaa5','pizza6']
for pizza in pizzas:
    print(pizza)
    print(f'我比较少吃{pizza}。\n')
print('1、玛格丽特披萨，是一种美味的美食，以脆皮披萨面皮、小番茄等为原料，以番茄酱汁等为调料。该美食主要通过烘烤的方法制作而成。\n'
      '2、至尊披萨，是意大利比萨的一个品种，至尊比萨从本质上改变了人们头脑中饼状比萨的传统概念，继承了意大利人的浪漫基因，'
      '就像吃一支冰淇淋一样，以最无拘无束的方式享用比萨，想站着吃就站着吃、想走着吃就走着吃，想怎么吃就怎么吃。\n'
      '3、鸡蛋香肠比萨，是一道美食，由意大利香肠、比萨面饼、鸡蛋等原料制作而成。')
print('---------切片---------')
print('The first three iterms in the list are:')
print(pizzas[0:3])
print('Three iterms from the middle of the list are:')
print(pizzas[1:4])
print('The last three iterms in the list are:')
print(pizzas[-3:])