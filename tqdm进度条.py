# Tsung
# 开发时间：2024/1/10 10:47
# Life is short,you need Python
# coding=utf-8

import time
from tqdm import tqdm, trange
import os

# for i in trange(100, desc="Training", unit='epoch'):
#     time.sleep(0.2)
#     print(f"{i}/Hello Python")

if __name__ == '__main__':
    for i in tqdm(range(100)):
        time.sleep(0.2)
        print(f"{i}//Hello Python")

        # os.system('cls')
