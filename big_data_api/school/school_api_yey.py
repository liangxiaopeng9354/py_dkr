# -*- coding: utf-8 -*-
# @Time    : 2024-8-14 10:38
# @Author  : liangxiaopeng
# @File    : school_api_yey.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = '幼儿园学校'
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtyey/school/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园"}  # 类型全选
data2 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "bxlxList": ["幼儿园"]}  # 类型幼儿园
data3 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "bxlxList": ["幼儿园"], "xzqyList": ["东城区"]}  # 类型幼儿园，区域选东城
data4 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "bxlxList": ["幼儿园"], "cxlxList": ["城市"]}  # 类型幼儿园，城乡类型选城市
data5 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "bxlxList": ["幼儿园"], "jbzlxList": ["教育部门"]}  # 类型幼儿园，教育部门
data6 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "bxlxList": ["幼儿园"], "sfphxmbyey": "普惠"}  # 类型幼儿园，普惠幼儿园
data7 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "cxlxList": ["城市"], "jbzlxList": ["教育部门"]}  # 类型幼儿园，普惠幼儿园,教育部门，城市
data8 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "cxlxList": ["农村"], "jbzlxList": ["教育部门"]}  # 类型幼儿园，普惠幼儿园,教育部门，城市
data9 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "cxlxList": ["农村"], "sfphxmbyey": "普惠"}  # 类型幼儿园，普惠幼儿园,教育部门，城市
data10 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "bxlxList": ["幼儿园"], "jbzlxList": ["集体"]}  # 类型幼儿园，教育部门
data11 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "cxlxList": ["城市"], "jbzlxList": ["部队"]}  # 类型幼儿园，教育部门
# 期望结果
num1 = 1989
num2 = 1989
num3 = 71
num4 = 1578
num5 = 494
num6 = 697
num7 = 339
num8 = 78
num9 = 47
num10 = 241
num11 = 73

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11}


def test_school_api_yey():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_school_api_yey()
