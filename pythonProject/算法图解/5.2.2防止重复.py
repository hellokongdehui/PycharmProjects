# coding=utf-8
# Author:D.辉
# Place：哈工深
# Time：2021/11/21 10:09

voted = {}


def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")


check_voter("lisa")
check_voter("jack")
check_voter("lisa")
