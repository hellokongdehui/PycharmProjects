# coding=utf-8
# Author:D.辉
# Place：哈工深
# Time：2021/11/16 23:16

import json
import datetime
import time

# 写入初始数据
# data = '[{"时间": "2021/04/18 18:59:41", "项目": "收到王敏货款", "金额": 20000, "分类": "收入"}, \
#         {"时间": "2021/04/18 19:59:41", "项目": "吃饭", "金额": 23.0, "分类": "支出"}, \
#         {"时间": "2021/04/18 20:00:12", "项目": "买手机", "金额": 4000.0, "分类": "支出"}, \
#         {"时间": "2021/04/18 21:03:32", "项目": "吃饭", "金额": 5.0, "分类": "支出"}, \
#         {"时间": "2021/04/18 21:06:07", "项目": "买菜", "金额": 34.0, "分类": "支出"}, \
#         {"时间": "2021/04/18 21:06:28", "项目": "发工资", "金额": 23000.0, "分类": "收入"}]'
#
# with open(r"data.txt", "w") as f:
#     f.write(data)

# 一个文本文件中只能保存一种业务对象


# 读json数据
import time


def readData():
    with open(r"data.txt", "r") as f:
        jsonData = f.read()
        dataList = json.loads(jsonData)
        return dataList


# 写json数据
def writeData(dataList):
    jsonData = json.dumps(dataList, ensure_ascii=False)
    with open(r"data.txt", "w") as f:
        f.write(jsonData)
        print("----数据更新成功！")


# 显示账目
def showData():
    sumIn = 0  # 总收入
    sumOut = 0  # 总支出
    dataList = readData()
    print("***********************************账单信息**************************************")
    for data in dataList:
        if data["分类"] == "收入":
            print(data["时间"], "   ", data["项目"], "   ", data["金额"], "   ", data["分类"])
            sumIn += data["金额"]
        else:
            print(data["时间"], "   ", data["项目"], "   ", data["金额"] * -1, "   ", data["分类"])
            sumOut += data["金额"]
    print("********************************************************************************")
    print("总收入为：", sumIn, "总支出为：", sumOut, "结余：", sumIn - sumOut)


# 增加账单信息
def addData():
    dataList = readData()
    content = input("请输入账单明细：")
    amount = float(input("请输入账单金额："))
    c = int(input("请选择（1.收入 2.支出）："))
    cla = "支出"
    if c == 1:
        cla = "收入"
    t = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    newData = {"时间": t, "项目": content, "金额": amount, "分类": cla}
    dataList.append(newData)
    writeData(dataList)


if __name__ == '__main__':
    while 1 == 1:
        showData()
        c = int(input('---如需新增账单请按“1"，退出请按”2“:'))
        if c == 1:
            addData()
        elif c == 2:
            print("---退出成功！")
            break
        else:
            print("---输入有误，请重新输入！")
        time.sleep(2)
        print('\n\n\n')
