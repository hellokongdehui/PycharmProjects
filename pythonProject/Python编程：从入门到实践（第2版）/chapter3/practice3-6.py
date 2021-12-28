# Author：D.H
# Place：哈工深
# Time：2021/7/24 17:57
#练习3-6：添加嘉宾
guests=['小明','小红','小乐']
print(f'Hello {guests[0]} 好久不见！改天共进晚餐啊！')
print(f'Hello {guests[1]} 好久不见！改天共进晚餐啊！')
print(f'Hello {guests[2]} 好久不见！改天共进晚餐啊！')

print('小乐回复说他没法参加晚宴,所以邀请小江来')

guests[-1]='小江' #邀请小江来替换小乐

print(f'Hello {guests[2]} 好久不见！改天共进晚餐啊！')

#或者以下方式替换
del guests[2]
guests.insert(2,'小江')
print(f'Hello {guests[2]} 好久不见！改天共进晚餐啊！')

print('找到了一个更大的餐桌，可以加多三人！')
guests.insert(0,'小黑')
guests.insert(2,'小白')
guests.append('小王')

#再次向每人发送邀请
print(f'Hello {guests[0]} 好久不见！改天共进晚餐啊！')
print(f'Hello {guests[1]} 好久不见！改天共进晚餐啊！')
print(f'Hello {guests[2]} 好久不见！改天共进晚餐啊！')
print(f'Hello {guests[3]} 好久不见！改天共进晚餐啊！')
print(f'Hello {guests[4]} 好久不见！改天共进晚餐啊！')
print(f'Hello {guests[5]} 好久不见！改天共进晚餐啊！')