# Author：D.H
# Place：哈工深
# Time：2021/7/19 16:41
#weeknameprint
weekstr='星期一星期二星期三星期四星期五星期六星期日'
weekid=eval(input('请输入星期数字（1-7）：'))
position=(weekid-1)*3
print(weekstr[position:position+3])
