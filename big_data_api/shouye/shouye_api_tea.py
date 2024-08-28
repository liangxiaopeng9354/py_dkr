# -*- coding: utf-8 -*-
# @Time    : 2024-8-19 10:38
# @Author  : liangxiaopeng
# @File    : shouye_api_tea.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "首页教师接口"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtxd/teacher/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
# 学生
data1 = {"nd":f"{synd}","xdfl":"学前教育","jzglx":"教职工"}
data2 = {"nd":f"{synd}","xdfl":"基础教育","jzglx":"教职工"}
data3 = {"nd":f"{synd}","xdfl":"职业教育","jzglx":"教职工"}
data4 = {"nd":f"{synd}","xdfl":"高等教育","jzglx":"教职工"}

# 期望结果
num1 = 96381
num2 = 169948
num3 = 8128
num4 = 160678

data_dict = {1: data1, 2: data2, 3: data3, 4: data4}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4}


# 执行方法
def test_shouye_api_tea():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_shouye_api_tea()
