# Author：D.H
# Place：哈工深
# Time：2021/7/17 11:07
#Q3：工作日的力量
dayup=1.0
dayfactor=0.01
for i in range(365): #采用循环模拟365天的过程，抽象+自动化
    if i % 7 in [6,0]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print('工作日每天进步百分之一的力量：{:.2f}'.format(dayup))