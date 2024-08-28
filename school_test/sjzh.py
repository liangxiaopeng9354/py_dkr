# -*- coding: utf-8 -*-
# @Time    : 2024-7-5 13:20
# @Author  : liangxiaopeng
# @File    : test1.py

def generate_combinations(lst):

    # 生成长度为2的所有组合
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            print([lst[i], lst[j]])

    # 生成长度为3的所有组合
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                print([lst[i], lst[j], lst[k]])

    # 生成长度为4的所有组合
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                for l in range(k + 1, len(lst)):
                    print([lst[i], lst[j], lst[k], lst[l]])

    # 生成长度为5的所有组合
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                for l in range(k + 1, len(lst)):
                    for m in range(l + 1, len(lst)):
                        print([lst[i], lst[j], lst[k], lst[l], lst[m]])

# 示例列表
my_list = [1, 2, 3, 4, 5]
# generate_combinations(my_list)
