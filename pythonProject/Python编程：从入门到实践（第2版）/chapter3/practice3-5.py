# Author：D.H
# Place：哈工深
# Time：2021/7/24 17:44
#练习3-5：修改嘉宾名单
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