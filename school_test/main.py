# -*- coding: utf-8 -*-
# @Time    : 2024-7-5 14:10
# @Author  : liangxiaopeng
# @File    : main.py
import dkr2
import sjzh2

def process_combination(combination):
    # 在这里处理每个组合
    # print(combination)
    for x in combination:
        list(x)
        if len(x) > 1:
            print(x[0],x[1])



with open('E:\\output1.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    length = len(parts)

    if length == 1:
        # 调用方法处理只有一个元素的组合
        pass
    elif length == 2:
        # 调用方法处理有两个元素的组合
        x = int(parts[0])
        y = int(parts[1])
        dkr2.generate_cartesian_product2('E:\\123.xlsx', x, y)
    elif length == 3:
        # 调用方法处理有三个元素的组合
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        dkr2.generate_cartesian_product3('E:\\123.xlsx', x, y, z)

    elif length == 4:
        # 调用方法处理有四个元素的组合
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        n = int(parts[3])
        dkr2.generate_cartesian_product4('E:\\123.xlsx', x, y,z, n)

    elif length == 5:
        # 调用方法处理有五个元素的组合
        print(parts,'-----------')
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        n = int(parts[3])
        m = int(parts[4])

        dkr2.generate_cartesian_product5('E:\\123.xlsx', x, y,z, n,m)
    elif length > 5:
        continue
