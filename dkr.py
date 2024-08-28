# -*- coding: utf-8 -*-
# @Time    : 2024-7-5 10:30
# @Author  : liangxiaopeng
# @File    : dkr.py


import itertools
import pandas as pd

# 读取Excel文件
df = pd.read_excel('E:\\123.xlsx', engine='openpyxl')


# 将数据转换为三个列表
list1 = df.iloc[:, 0].dropna().tolist()  # 第一列数据
list2 = df.iloc[:, 1].dropna().tolist()  # 第二列数据
list3 = df.iloc[:, 2].dropna().tolist()  # 第三列数据
list4 = df.iloc[:, 3].dropna().tolist()  # 第四列数据
list5 = df.iloc[:, 4].dropna().tolist()  # 第五列数据



# 计算笛卡尔积
cartesian_product = itertools.product(list1, list2, list3, list4, list5)

# 将笛卡尔积转换为字符串并用'-'分隔
result = [''.join(item) for item in cartesian_product]

# 将结果写入txt文件
with open('E:\\output.txt', 'w') as f:
    for line in result:
        f.write(line + '\n')