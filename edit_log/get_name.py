# -*- coding: utf-8 -*-
# @Time    : 2024-8-6 10:01
# @Author  : liangxiaopeng
# @File    : edit_log_select.py

import pandas as pd
from pypinyin import pinyin, Style


def name_to_pinyin(name):
    """将名字转换为全拼，并去除声调"""
    return ''.join([word[0] for word in pinyin(name, style=Style.NORMAL)])


# 读取Excel文件
file_path = 'C:/Users/lxp/Desktop/123.xlsx'  # 替换为你的Excel文件路径
df = pd.read_excel(file_path)

# 假设第一列的名字在'A'列，我们将其转换为全拼并存储在'B'列
df['全拼'] = df.iloc[:, 0].apply(name_to_pinyin)

# 将修改后的DataFrame写回Excel文件，可以选择覆盖原文件或保存为新文件
df.to_excel('C:/Users/lxp/Desktop/1234.xlsx', index=False)  # 替换为你的新文件路径

print("Excel文件已更新，全拼已添加到第二列。")
