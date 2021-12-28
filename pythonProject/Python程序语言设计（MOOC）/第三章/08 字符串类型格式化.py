# Author：D.H
# Place：哈工深
# Time：2021/7/20 8:41
#格式化是对字符串进行格式表达的方式
'''
字符串格式化使用.format()方法，用法如下：
<模板字符串>.format(<逗号分隔的参数>)
'''

#槽
a='{}:计算机{}的CPU占用率为{}%'.format('2021/07/20','a','20') #字符串中槽{}和format()中参数的默认顺序为：0 ，1 ，2
b='{0}:计算机{2}的CPU占用率为{1}%'.format('2021/07/20','a','20') #可更换顺序
print(a)
print(b)

#format（）方法的格式控制
#槽内部对格式化的配置方式
#{<参数序号>:<格式控制标记>}

hanshu1='python'
print('{0:=^20}'.format(hanshu1)) # ^ 居中对齐
print('{0:=^20}'.format('hanshu1')) #注意两者差别

hanshu2='BAT'
print('{0:*>20}'.format(hanshu2)) # > 右对齐 < 左对齐
print('{0:*>20}'.format('BAT'))

hanshu3='bitdance'
print('{:10}'.format(hanshu3)) #槽设定的宽度为10
print('{:10}'.format('bitdance'))

hanshu4=float('123456.7890') #加了个float 浮点数类型
print('{:.2f}'.format(hanshu4))
print(float('{:.2f}'.format(123456.7890)))

#类型
print('{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}'.format(425)) # b:二进制，c：字符形式、Unicode编码形式，d：十进制，o：八进制，x：十六进制，X：大写的十六进制

#科学计数法
print('{0:e},{0:E},{0:f},{0:%}'.format(3.14)) #科学计数法小e，大E,非科学计数法，百分比的形式