# Author：D.H
# Place：哈工深
# Time：2021/7/24 18:13
#练习3-7：缩减名单
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

print('非常抱歉！由于餐桌没到，只能两位共进晚餐！')
podded1=guests.pop()
print(f'{podded1},非常不好意思，由于新餐桌没到，所以不能邀请您共进晚餐了！')
podded2=guests.pop(-2)
print(f'{podded2},非常不好意思，由于新餐桌没到，所以不能邀请您共进晚餐了！')
podded3=guests.pop(-2)
print(f'{podded3},非常不好意思，由于新餐桌没到，所以不能邀请您共进晚餐了！')
podded4=guests.pop(0)
print(f'{podded4},非常不好意思，由于新餐桌没到，所以不能邀请您共进晚餐了！')

#发送给余下两位嘉宾邀请
print(f'Hello {guests[0]} 好久不见！改天共进晚餐啊！')
print(f'Hello {guests[1]} 好久不见！改天共进晚餐啊！')

print('删除两位嘉宾')
del guests[0]
del guests[0]
print(guests) #核实是否为空
