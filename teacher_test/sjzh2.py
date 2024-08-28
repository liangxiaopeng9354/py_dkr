# -*- coding: utf-8 -*-
# @Time    : 2024-7-5 13:20
# @Author  : liangxiaopeng
# @File    : test1.py
import os

# 获取当前文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 指定你想要生成文件的目录
output_dir = os.path.join(current_dir, 'data')

# 确保目录存在
os.makedirs(output_dir, exist_ok=True)

# 生成文件的路径
output_file_path = os.path.join(output_dir, 'output1-9.txt')


def generate_combinations(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n + 1):
            combination = nums[i:j]
            result.append(combination)
    return result


if __name__ == '__main__':

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    combinations = generate_combinations(nums)

    # 将结果写入txt文件
    with open(output_file_path, 'w') as f:
        for combination in combinations:
            f.write(','.join(map(str, combination)) + '\n')
