# Author：D.H
# Place：哈工深
# Time：2021/7/25 10:48
#练习4-6：奇数
#列表解析法
jishu=[js for js in range(1,21,2)]
print(jishu)

#方法2
jushu1=[]
for js1 in range(1,21,2):
    print([js1])
    jushu1.append(js1)
print(jushu1)
