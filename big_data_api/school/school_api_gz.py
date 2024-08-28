# -*- coding: utf-8 -*-
# @Time    : 2024-8-14 10:38
# @Author  : liangxiaopeng
# @File    : school_api_gz.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = '基础教育高中学校'
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtgz/school/summaryInfo'
headers = HEADERS
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中"}
data2 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "bxlxList": ["十二年一贯制学校"]}
data3 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "bxlxList": ["十二年一贯制学校", "高级中学", "完全中学"]}
data8 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jbzlxList": ["具有法人资格的中外合作办学及内地与港澳地区合作办学"]}
data9 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "cxlxList": ["城市"], "jbzlxList": ["教育部门"]}
data4 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "xzqyList": ["东城区"]}
data5 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "cxlxList": ["城市"]}
data6 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jbzlxList": ["教育部门"]}
data7 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "bxtjdbfl": "tyydcmjsfdb"}

# 期望结果
num1 = 351
num2 = 137
num3 = 351
num4 = 30
num5 = 311
num6 = 262
num7 = 271
num8 = 4
num9 = 240

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9}


def test_school_api_gz():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_school_api_gz()
