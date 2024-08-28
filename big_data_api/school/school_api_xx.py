# -*- coding: utf-8 -*-
# @Time    : 2024-8-14 10:38
# @Author  : liangxiaopeng
# @File    : school_api_xx.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = '基础教育小学学校'
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtxx/school/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data8 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学"}
data1 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "bxlxList": ["小学"]}  # 类型全选
data2 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "bxlxList": ["小学"], "xzqyList": ["东城区", "西城区"]}  # 西城，东城
data3 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "bxlxList": ["小学"], "xzqyList": ["东城区"]}  # 区域选东城
data4 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "bxlxList": ["小学"], "cxlxList": ["城市"]}  # 城乡类型选城市
data5 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "bxlxList": ["小学"], "jbzlxList": ["教育部门"]}  # 教育部门
data6 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "bxlxList": ["小学"], "cxlxList": ["县镇"],
         "jbzlxList": ["教育部门"]}  # 县镇的教育部门
data7 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "bxlxList": ["小学"], "bxtjdbfl": "tyydcmjsfdb"}  # 体育运动场(馆)面积达标


# 期望结果
num1 = 719
num2 = 103
num3 = 45
num4 = 546
num5 = 677
num6 = 72
num7 = 521
num8 = 719

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8}



def test_school_api_xx():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_school_api_xx()
