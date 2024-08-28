# -*- coding: utf-8 -*-
# @Time    : 2024-8-6 10:01
# @Author  : liangxiaopeng
# @File    : edit_log_select.py

import pandas as pd

# 定义日志文件路径和输出Excel文件路径
log_file_path = 'E:/123.log'
output_excel_path = 'E:/output_sql_time.xlsx'

# 初始化一个空的DataFrame来存储结果
df = pd.DataFrame(columns=['SQL 语句', '执行时间'])

# 读取文件并解析
with open(log_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()  # 读取所有行到列表中
    group = []  # 用于存储当前组的行
    for line in lines:
        line = line.strip()

        # 检查是否为新组的开始（以'2024'开头的时间戳）
        if line.startswith('2024'):
            # 如果当前组非空，则处理它
            if group:
                # 提取时间戳和SQL语句
                timestamp = group[0][:19]  # 假设时间戳总是每组的第一行，并且长度固定为19
                sql_statement = None
                for line_in_group in group:
                    if line_in_group.startswith('select'):
                        sql_statement = line_in_group
                        break

                        # 如果找到了SQL语句，则添加到DataFrame
                if sql_statement:
                    df = df.append({'SQL 语句': sql_statement, '执行时间': timestamp}, ignore_index=True)

                    # 重置当前组
                group = []

                # 将新的时间戳行添加到当前组
            group.append(line)

            # 如果当前行是SQL语句，则也添加到当前组
        elif line.startswith('select'):
            group.append(line)

            # 处理最后一组数据（如果文件以SQL语句或时间戳之外的行结束）
    if group:
        timestamp = group[0][:19]  # 假设最后一组的时间戳也是第一行
        sql_statement = None
        for line_in_group in group:
            if line_in_group.startswith('select'):
                sql_statement = line_in_group
                break

        if sql_statement:
            df = df.append({'SQL 语句': sql_statement, '执行时间': timestamp}, ignore_index=True)

        # 写入Excel文件
df.to_excel(output_excel_path, index=False, engine='openpyxl')

print(f"数据已写入 {output_excel_path}")