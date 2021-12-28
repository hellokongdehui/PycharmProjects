# Author：D.H
# Place：哈工深
# Time：2021/7/28 16:47
# 练习6-5：河流
rivers = {'nile': 'egypt', 'yangtzi river': 'hubei', 'pearl river': 'guangdong', }
for river, place in rivers.items():
    print(f'The {river.title()} runs through {place.title()}.')

for river in rivers.keys():
    print('\n'+river.title())

for place in rivers.values():
    print('\n'+place)