# Author：D.H
# Place：哈工深
# Time：2021/7/20 7:21
#一些以函数形式提供的字符串处理功能

hanshu='456一二三'
print(len(hanshu)) #len（x）函数，返回字符串x的长度

hanshu1=[1,2]
print(str(hanshu),str(hanshu1)) #任意类型x所对应的字符串形式

hanshu2=425
print(hex(hanshu2),oct(hanshu2)) #整数x的十六进制或八进制小写形式字符串

hanshu3='1+1=2'+chr(1004)  #chr(u)函数，u为Unicode编码，返回其对应的字符
print(hanshu3)

hanshu4='这个字符Ϭ的Unicode值是：'+str(ord('Ϭ')) #x为字符，返回其对应的Unicode编码
print(hanshu4)

for i in range(12):
    print(chr(9800+i),end='') #12星座，循环12次，每次循环+1，end='' 等于空不换行
#Unicode》》chr（u）》》单字符，单字符》》ord（x）》》Unicode

print('---------------------')
#一些以方法形式提供的字符串处理功能

hanshu5='ABCDefgh'
print(str.lower(hanshu5),str.upper(hanshu5)) #返回字符串副本，全部字符小写/大写

hanshu6='A,B,C'.split() #str.split(sep=None)，返回一个列表，由str根据sep被分隔的部分组成
print(hanshu6)

hanshu7='an apple a day'
print(hanshu7.count('a')) #str.count(sub)，返回子串在str中出现的次数

hanshu8='abcdefg123456'
print(hanshu8.replace('a','A')) #str.replace（old，new），返回字符串str副本，所有old子串被替换为new

hanshu9='python'
print(hanshu9.center(20,'=')) #str.center(width,fillchar），字符串str根据宽度width居中，fillchar为可选内容

hanshu10='==python123=='
print(hanshu10.strip('=123p')) #str.strip（chars），从str中去掉在其左侧和右侧chars中列出的字符

hanshu11='A'
print(hanshu11.join('123456')) #str.join(iter)，在iter变量除最后元素外每个元素后增加一个str