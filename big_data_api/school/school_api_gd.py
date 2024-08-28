# -*- coding: utf-8 -*-
# @Time    : 2024-8-14 10:38
# @Author  : liangxiaopeng
# @File    : school_api_gd.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = '高等教育学校'
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtgx/school/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data4 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "bxlxList": ["大学"]}
data5 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "bxlxList": ["学院"]}
data6 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "bxlxList": ["独立学院"]}
data7 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "bxlxList": ["高等专科学校"]}
data8 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "bxlxList": ["高等职业学校"]}
data1 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "bxlxList": ["大学", "学院", "独立学院", "高等专科学校", "高等职业学校"]}  # 类型全选
data2 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "cxlxList": ["城市", "县镇", "农村", "其他"]}  # 城乡类型全选
data3 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jbzlxList": ["教育部门", "其他部门", "其他", "民办", "地方企业"]}


# 期望结果
num1 = 92
num2 = 92
num3 = 92
num4 = 37
num5 = 25
num6 = 5
num7 = 1
num8 = 24

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7}


def test_school_api_gd():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_school_api_gd()
