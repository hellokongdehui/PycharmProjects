# decoding=utf-8
# Author:D.辉
# Place：哈工深
# Time：2021/12/28 22:46

# 银行卡类
# 属性：银行名称，卡号，密码，姓名，余额
# 方法：登录，存款


class Card():
    def __init__(self, cnum, cpwd, cname, cbalance):
        self.bankName = "python银行"
        self.cnum = cnum
        self.cpwd = cpwd
        self.cname = cname
        self.cbalance = cbalance

    def login(self):
        num = input("请输入卡号：")
        pwd = input("请输入密码：")
        if num == self.cnum and pwd == self.cpwd:
            print("登录成功！")
            return "ok"
        else:
            print("验证失败！")
            return "no"

    def deposit(self):
        r = self.login()  # 在类的内部调用其他方法，使用self作为对象名
        if r == "ok":
            money = float(input("请输入存款金额："))
            self.cbalance += money
            print("存款成功！存入", money, "元，余额：", self.cbalance, "元！")


card1 = Card("10001", "123456", "令狐冲", 10000)
card2 = Card("10002", "123456", "诸葛亮", 6000)

card1.deposit()
