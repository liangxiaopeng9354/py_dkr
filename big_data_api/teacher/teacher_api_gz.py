# -*- coding: utf-8 -*-
# @Time    : 2024-8-15 16:11
# @Author  : liangxiaopeng
# @File    : teacher_api_gz.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "高中老师"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtgz/teacher/summaryInfo'
headers = HEADERS # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jzglx": "专任教师", "jzgxl": "博士研究生"}
data2 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jzglx": "专任教师", "jzgxl": "专科毕业"}
data3 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jzglx": "专任教师", "zyjszw": "正高级"}
data4 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jzglx": "专任教师", "zyjszw": "正高级", "nlfd": "50-54岁"}
data5 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jzglx": "专任教师", "zyjszw": "员级", "nlfd": "35-39岁"}
data6 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jzglx": "专任教师", "zyjszw": "中级", "nlfd": "35-39岁"}
data7 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jzglx": "专任教师", "zyjszw": "助理级", "nlfd": "35-39岁"}
data8 = {"nd": f"{nd}", "xdfl": "基础教育", "cxlxList": ["城市", "县镇", "农村", "其他"], "xdzl": "普通高中", "jzglx": "专任教师"}
data9 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jzglx": "专任教师"}
data10 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "jzglx": "教职工"}
data11 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通高中", "bxlxList": ["十二年一贯制学校", "高级中学", "完全中学"], "jzglx": "教职工"}

# 期望结果
num1 = 897
num2 = 34
num3 = 293
num4 = 139
num5 = 6
num6 = 1712
num7 = 814
num8 = 54382
num9 = 54382
num10 = 68899
num11 = 68899

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11}


# 执行方法
def test_teacher_api_gz():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_teacher_api_gz()
