# -*- coding: utf-8 -*-
# @Time    : 2024-8-14 10:38
# @Author  : liangxiaopeng
# @File    : school_api_cz.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "普通教育初中学校"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtcz/school/summaryInfo'
headers = HEADERS  # 设置请求头为JSON

# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中"}  # 类型全选
data2 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "bxlxList": ["九年一贯制学校"]}
data3 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "bxlxList": ["九年一贯制学校", "初级中学"]}
data4 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "xzqyList": ["东城区"]}
data5 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "cxlxList": ["城市"]}
data6 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "jbzlxList": ["教育部门"]}
data7 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "bxtjdbfl": "tyydcmjsfdb"}
data8 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "cxlxList": ["城市"], "bxtjdbfl": "tyydcmjsfdb"}

# 期望结果
num1 = 333
num2 = 157
num3 = 333
num4 = 8
num5 = 208
num6 = 306
num7 = 303
num8 = 180

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8}


def test_school_api_cz():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_school_api_cz()
