# -*- coding: utf-8 -*-
# @Time    : 2024-8-14 10:38
# @Author  : liangxiaopeng
# @File    : student_api_yey.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "学前教育学生"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtyey/student/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "zbz": "在校生"}  # 在校生
data2 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "zbz": "招生"}  # 招生
data3 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "zbz": "毕业生"}  # 毕业生
data4 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "xzqyList": ["东城区"], "zbz": "在校生"}  # 东城区在校生
data5 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "xzqyList": ["东城区"], "zbz": "招生"}  # 东城区招生
data6 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "xzqyList": ["东城区"], "zbz": "毕业生"}  # 东城区毕业生
data7 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "zbz": "在校生", "nj": "托班"}  # 托班
data8 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "jbzlxList": ["教育部门"], "zbz": "在校生"}  # 教育部门在校生
data9 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "zbz": "在校生", "sfphxmbyey": "普惠"}  # 普惠在校生
data10 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "cxlxList": ["城市"], "zbz": "在校生"}  # 城区在校生
data11 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "cxlxList": ["城市"], "jbzlxList": ["其他部门"],
          "zbz": "在校生"}  # 城市的其他部门的在校生
data12 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "zbz": "在校生", "sfgjxs": "国际学生"}  # 国际在校生
data13 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "cxlxList": ["城市"], "jbzlxList": ["教育部门"],
          "zbz": "在校生"}  # 城市的教育部门
data14 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "cxlxList": ["城市"], "jbzlxList": ["教育部门"], "zbz": "在校生",
          "nj": "混合班"}  # 混合班城区教育部门
data15 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "cxlxList": ["城市"], "jbzlxList": ["民办"], "zbz": "在校生",
          "nj": "大班"}  # 城市民办大班
data16 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "cxlxList": ["城市"], "jbzlxList": ["部队"], "zbz": "在校生",
          "nj": "小班"}
data17 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "jbzlxList": ["具有法人资格的中外合作办学及内地与港澳地区合作办学"], "zbz": "在校生"}


# 期望结果
num1 = 574235
num2 = 178620
num3 = 162717
num4 = 19455
num5 = 5846
num6 = 6047
num7 = 996
num8 = 190292
num9 = 195928
num10 = 485308
num11 = 21254
num12 = 775
num13 = 145264
num14 = 103
num15 = 82431
num16 = 6651
num17 = 306

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11, 12: data12, 13: data13, 14: data14, 15: data15, 16: data16,17:data17}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11,
            12: num12, 13: num13, 14: num14, 15: num15, 16: num16,17:num17}


# 执行方法
def test_student_api_yey():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_student_api_yey()
