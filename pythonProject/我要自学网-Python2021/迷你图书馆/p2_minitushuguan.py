# Author:D.辉
# Place：哈工深
# Time：2021/11/14 15:13

import json
import datetime
import time

# 写入初始数据
# d1 = '[{"用户名": "admin", "密码": "123456", "姓名": "张三"},{"用户名": "aaa", "密码": "123456", "姓名": "李四"},'\
#     '{"用户名": "bbb", "密码": "123456", "姓名": "王五"}]'
#
# with open(r"users.txt", "w") as f:
#     f.write(d1)
#
# d2 = '[{"编号": 1001, "书名": "《红楼梦》", "作者": "曹雪芹", "借出状态": "可借"}, \
# {"编号": 1002, "书名": "《Java教程》", "作者": "齐一天", "借出状态": "可借"}, \
# {"编号": 1003, "书名": "《声景》", "作者": "沙佛", "借出状态": "已借出"}, \
# {"编号": 1004, "书名": "《程序员修炼之道》", "作者": "电子工业", "借出状态": "可借"}]'
#
# with open(r"book.txt", "w") as f:
#     f.write(d2)


# 读json数据
def readUsers():
    with open(r"users.txt", "r") as f:
        jsonData = f.read()
    dataList = json.loads(jsonData)
    return dataList


def readData():
    with open(r"book.txt", "r") as f:
        jsonData = f.read()
    dataList = json.loads(jsonData)
    return dataList


# 写json数据
def writeData(dataList):
    jsonData = json.dumps(dataList, ensure_ascii=False)
    with open(r"book.txt", "w") as f:
        f.write(jsonData)
        print("---数据更新成功！")


def writeUsers(userLists):
    jsonDate = json.dumps(userLists, ensure_ascii=False)
    with open(r"users.txt", "w") as f:
        f.write(jsonDate)
        print("---数据写入成功！")


# 用户登录； login()
def login():
    msg = '失败'
    userLists = readUsers()
    name = input("请输入用户名：")
    pwd = input("请输入密码：")
    for user in userLists:
        if name == user['用户名'] and pwd == user['密码']:
            print("---恭喜您登录成功！", user['姓名'], '!')
            msg = '成功'
            break
    if msg == '失败':
        print("---验证失败！")
    return msg
    print('************************************')


# 注册（在数据库中增加用户）
def reg():
    name = input("请输入新用户名：")
    password = input("请输入密码：")
    newUser = {"uname": name, "upwd": password}  # 新用户
    userLists = readUsers()
    userLists.append(newUser)  # 将新用户添加到用户列表
    writeUsers(userLists)
    print("---注册成功！")

# 1.显示所有图书
def showAllBooks():
    print('************************************')
    bookLists = readData()
    for book in bookLists:
        print(book['编号'], book['书名'], book['作者'], book['借出状态'])
    print('************************************')


# 2.图书上架
def addBook():
    bookLists = readData()
    newList = []
    for book in bookLists:
        newList.append(book['编号'])
    newNum = max(newList)+1
    bookName = input('请输入书名：')
    bookName = "《"+bookName+"》"
    author = input('请输入作者：')
    state = '可借'
    newBook = {"编号": newNum, "书名": bookName, "作者": author, "借出状态": state}
    bookLists.append(newBook)
    writeData(bookLists)
    print('************************************')


# 3.图书下架
def delBook():
    bookLists = readData()
    data1 = int(input('请输入要下架的图书编号：'))
    data2 = input('或输入要下架的图书名称：')
    for book in bookLists:
        if data1 == book['编号'] or data2 == book['书名']:
            bookLists.remove(book)  # 删除图书信息
            print('---图书', book['书名'], '下架成功！')
    writeData(bookLists)
    print('************************************')


# 4.借书
def lendBook():
    bookLists = readData()
    bookName = input('请输入要借的图书名称：')
    msg = 0  # 0没有 1可借 2不可借
    for book in bookLists:
        if bookName == book['书名']:
            msg = 2
            if book['借出状态'] == '可借':
                print('---您已成功借出', book['书名'], '！')
                book['借出状态'] = "已借出"
            else:
                print(book['书名'], '已借出', '请下次再来')
    if msg == 0:
        print('---没有此图书！')
    writeData(bookLists)
    print('************************************')


# 5.还书
def returnBook():
    bookLists = readData()
    num = int(input('请输入要归还的图书编号：'))
    msg = 0
    for book in bookLists:
        if num == book['编号']:
            msg = 2
            if book['借出状态'] == '已借出':
                print('---成功归还图书', book['书名'], '!')
                book['借出状态'] = '可借'
            else:
                print('---该书无需归还！')
    if msg == 0:
        print('---没有此图书！')
    writeData(bookLists)
    print('************************************')


# 6.主函数
def main():
    print('******************图书管理系统v1.0*******************')
    msg = login()
    msg = "成功"
    if msg == "成功":
        while 0 == 0:
            print("1.显示所有图书\n2.图书上架\n3.图书下架\n4.借书\n5.还书\n6.退出 ")
            print("***************************************************")
            c = int(input("请输入业务编号（1-6）："))
            if c == 1:
                showAllBooks()
            elif c == 2:
                addBook()
            elif c == 3:
                delBook()
            elif c == 4:
                lendBook()
            elif c == 5:
                returnBook()
            elif c == 6:
                break
            else:
                print("没有此业务！")


if __name__ == '__main__':
    main()

