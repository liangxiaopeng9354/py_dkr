# -*- coding: utf-8 -*-
# @Time    : 2024-8-14 10:38
# @Author  : liangxiaopeng
# @File    : school_api_gz.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = '职业教育学校'

# 定义API URL
url = f'{ip}api/sjfx/itemData/gtzz/school/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职"}  # 类型全选
data2 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"]}  # 中等技术学校
data3 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职",
         "bxlxList": ["中等技术学校", "成人中等专业学校", "职业高中学校"]}  # 中等技术学校/成人中等专业学校/职业高中学校
data4 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "xzqyList": ["东城区"]}  # 东城区
data5 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "jbzlxList": ["民办"]}  # 城区的普通初中
data6 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"],
         "jbzlxList": ["中央教育部门", "中央其他部门"]}  # 中央教育部门
data7 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"],
         "jbzlxList": ["省级其他部门", "县级其他部门"]}  # 其他部门学校

# 期望结果
num1 = 77
num2 = 28
num3 = 77
num4 = 4
num5 = 17
num6 = 7
num7 = 13

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7}


def test_school_api_zhiye():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_school_api_zhiye()
