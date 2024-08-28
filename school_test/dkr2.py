# -*- coding: utf-8 -*-
# @Time    : 2024-7-5 10:30
# @Author  : liangxiaopeng
# @File    : dkr.py

import sjzh
import pandas as pd
from itertools import product

def read_excel_and_convert_to_lists(file_path):
    df = pd.read_excel(file_path)
    column1 = df.iloc[:, 0].dropna().tolist()
    column2 = df.iloc[:, 1].dropna().tolist()
    column3 = df.iloc[:, 2].dropna().tolist()
    column4 = df.iloc[:, 3].dropna().tolist()
    column5 = df.iloc[:, 4].dropna().tolist()
    column6 = df.iloc[:, 5].dropna().tolist()
    column7 = df.iloc[:, 6].dropna().tolist()
    column8 = df.iloc[:, 7].dropna().tolist()
    column9 = df.iloc[:, 8].dropna().tolist()
    return column1, column2, column3, column4, column5,column6,column7,column8,column9

def generate_cartesian_product2(file_path, col1, col2):
    print(col1,'----111111111111111111')
    # print(col2,'----111111111111111111')
    # print(col3,'----111111111111111111')
    # print(type(col1))
    columns = read_excel_and_convert_to_lists(file_path)
    cartesian_product = list(product(columns[col1 - 1], columns[col2 - 1]))
    result = [''.join(item) for item in cartesian_product]
    with open('data/output.txt', 'a') as f:
        for line in result:
            f.write(line + '\n')


def generate_cartesian_product3(file_path, col1, col2, col3):
    print(col1,'----111111111111111111')
    # print(col2,'----111111111111111111')
    # print(col3,'----111111111111111111')
    # print(type(col1))
    columns = read_excel_and_convert_to_lists(file_path)
    cartesian_product = list(product(columns[col1 - 1], columns[col2 - 1], columns[col3 - 1]))
    result = [''.join(item) for item in cartesian_product]
    with open('data/output.txt', 'a') as f:
        for line in result:
            f.write(line + '\n')

def generate_cartesian_product4(file_path, col1, col2, col3,col4):
    print(col1,'----111111111111111111')
    # print(col2,'----111111111111111111')
    # print(col3,'----111111111111111111')
    # print(type(col1))
    columns = read_excel_and_convert_to_lists(file_path)
    cartesian_product = list(product(columns[col1 - 1], columns[col2 - 1], columns[col3 - 1], columns[col4 - 1]))
    result = [''.join(item) for item in cartesian_product]
    with open('data/output.txt', 'a') as f:
        for line in result:
            f.write(line + '\n')

def generate_cartesian_product5(file_path, col1, col2, col3,col4,col5):
    print(col1,'----111111111111111111')
    # print(col2,'----111111111111111111')
    # print(col3,'----111111111111111111')
    print(type(col1))
    columns = read_excel_and_convert_to_lists(file_path)
    cartesian_product = list(product(columns[col1 - 1], columns[col2 - 1], columns[col3 - 1], columns[col4 - 1], columns[col5 - 1]))
    result = [''.join(item) for item in cartesian_product]
    with open('data/output.txt', 'a') as f:
        for line in result:
            f.write(line + '\n')
# # 脚本1：读取Excel文件并转换为列表
# column1, column2, column3, column4, column5 = read_excel_and_convert_to_lists('E:\\123.xlsx')
# print(column1, column2, column3, column4, column5)


# # 脚本2：根据用户输入的列数生成笛卡尔积并输出到txt文件
# col1 = int(input("请输入第一列的索引（从1开始）："))
# col2 = int(input("请输入第二列的索引（从1开始）："))
# col3 = int(input("请输入第二列的索引（从1开始）："))

# # 调用生成随机列的方法
# my_list = [1, 2, 3, 4, 5]
#
# x = sjzh.generate_combinations(my_list)


