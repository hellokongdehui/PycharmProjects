# decoding=utf-8
# Author:D.辉
# Place：哈工深
# Time：2021/12/28 22:46

# 银行卡类
# 属性：银行名称，卡号，密码，姓名，余额
# 方法：登录，存款
# 将类中的属性或方法私有化，私有化的属性和方法只能在类的内部被调用

class Card():
    def __init__(self, cnum, cpwd, cname, cbalance):
        self.bankName = "python银行"
        self.cnum = cnum
        self.cpwd = cpwd
        self.cname = cname
        self.__cbalance = cbalance  # 已封装，属于私有属性

    def __login(self):  # 私有方法
        num = input("请输入卡号：")
        pwd = input("请输入密码：")
        if num == self.cnum and pwd == self.cpwd:
            print("登录成功！")
            return "ok"
        else:
            print("验证失败！")
            return "no"

    def deposit(self):
        r = self.__login()  # 在类的内部调用其他方法，使用self作为对象名
        if r == "ok":
            money = float(input("请输入存款金额："))
            self.__cbalance += money
            print("存款成功！存入", money, "元，余额：", self.__cbalance, "元！")

    def showBalance(self):
        r = self.__login()
        if r == "ok":
            print("余额：", self.__cbalance, "元")


card1 = Card("10001", "123456", "令狐冲", 10000)
card2 = Card("10002", "123456", "诸葛亮", 6000)

card1.deposit()
card2.showBalance()
