# -*- coding: utf-8 -*-
# @Time    : 2024-7-5 13:20
# @Author  : liangxiaopeng
# @File    : test1.py

def generate_combinations(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n + 1):
            combination = nums[i:j]
            result.append(combination)
    return result


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

combinations = generate_combinations(nums)

# 将结果写入txt文件
with open('E:\\output1.txt', 'w') as f:
    for combination in combinations:
        f.write(','.join(map(str, combination)) + '\n')
