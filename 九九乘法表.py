# Tsung
# 开发时间：2024/1/11 12:42
# Life is short,you need Python
# coding=utf-8
print('****************************while实现********************************')
i = 1
while i < 10:
    j = 1
    while j < i + 1:
        print(f"{j}*{i}={i * j}", end='\t')
        j += 1
    i += 1
    print()
print("***********************************************************")
i = 1
while i < 10:
    j = i
    while j < 10:
        print(f"{i}*{j}={j * i}", end='\t')
        j += 1
    print()
    i += 1
print("*************************************************************")
print("*******************for循环实现如下*****************************")
print("**************************************************************")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}", end='\t')
    print()
print("**********************************************************")
for i in range(1, 10):
    for j in range(i, 10):
        print(f"{i}*{j}={i * j}", end='\t')
    print()
