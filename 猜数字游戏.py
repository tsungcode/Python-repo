# Tsung
# 开发时间：2024/1/11 13:38
# Life is short,you need Python
# coding=utf-8
import random


def playGame():
    pass


print('\033[1;32m', end='')  # green
print('*' * 50)
print('*' * 50)
print('\033[0m', end='')  # end green
print('\033[1;31m', end='')  # red
print("欢迎来玩猜数字游戏！总共有6次机会")
print('\033[0m', end='')  # end red
print('\033[1;32m', end='')  # green
print('*' * 50)
print('*' * 50)
print('\033[0m', end='')  # end green
cont = 0
var = 6
number = random.randint(1, 100)

while True:
    cont += 1
    if var == 0:
        print('\033[1;32m', end='')  # green
        print(f"很遗憾！你可用的猜数字游戏机会为{var}")
        print("你个大笨蛋，蠢货，滚去好好学习吧！")
        print('\033[0m', end='')  # end green
        break
    else:
        print(f"温馨提示，您还有:{var}次机会,祝你好运！")
        num = eval(input("请输入一个：1——100之间的数>>"))
        var -= 1
        if number == num:
            print('\033[1;31m', end='')  # red
            print("哇哦，好聪明哦，恭喜您猜对了！！！！")
            print(f"本次猜数字游戏您总共用了：{cont}次就通过了！")
            print('\033[0m', end='')  # end red
            break
        elif num > number:
            print("您猜大了哦！")
            continue
        elif num < number:
            print("您猜小了哦！")
            continue
        else:
            print('\033[1;31m', end='')  # red
            print("哇哦，好聪明哦，恭喜您猜对了！！！！")
            print(f"本次猜数字游戏您总共用了：{cont}次就通过了！")
            print('\033[0m', end='')  # end red
