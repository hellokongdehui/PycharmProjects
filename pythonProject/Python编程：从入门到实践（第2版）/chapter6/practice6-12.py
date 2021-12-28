# Author：D.H
# Place：哈工深
# Time：2021/7/29 15:22
# 练习6-13：扩展
alien_0 = {'color': 'green', 'speed': 'slow' }
alien_0['color'] = 'yellow' #修改值
print(alien_0['color'])

# print(alien_0['points']) KeyError: 'points' 不存在points，错误

point_value = alien_0.get('point', 'No point value assigned.') # get() 第一个参数用于指定值，第二个参数为指定键不存在时的返回值。
print(point_value)

