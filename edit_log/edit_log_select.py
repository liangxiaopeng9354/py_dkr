# -*- coding: utf-8 -*-
# @Time    : 2024-8-5 20:01
# @Author  : liangxiaopeng
# @File    : edit_log_select.py

import re
import pandas as pd

# 读取日志文件
with open('E:/10时04分10秒_副本_debug.log', 'r',encoding='utf-8') as file:
    lines = file.readlines()

# 匹配以"select"开头的行
pattern = re.compile(r'^select.*$', re.IGNORECASE)
selected_lines = [line.strip() for line in lines if pattern.match(line)]


# 将匹配到的数据写入Excel文件
df = pd.DataFrame(selected_lines, columns=['SQL'])
df.to_excel('E:/20240807_sql.xlsx', index=False)



