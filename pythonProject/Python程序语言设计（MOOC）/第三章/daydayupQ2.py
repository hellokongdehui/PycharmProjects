# Author：D.H
# Place：哈工深
# Time：2021/7/17 10:56
#Q2
dayfactor=0.005
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print('向上千分之五：{:.2f},向下千分之五：{:.2f}'.format(dayup,daydown))