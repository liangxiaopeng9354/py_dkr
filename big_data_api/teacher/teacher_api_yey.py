# -*- coding: utf-8 -*-
# @Time    : 2024-8-15 13:28
# @Author  : liangxiaopeng
# @File    : teacher_api_yey.py

# 册子p156

from tool.api_response_tool import test_api_response
from tool.api_dic import *

name = "学前教育幼儿园老师"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtyey/teacher/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "jzglx": "教职工"}
data2 = {"nd": f"{nd}", "xdfl": "学前教育", "jbzlxList": ["教育部门"], "xdzl": "幼儿园", "jzglx": "教职工"}
data3 = {"nd": f"{nd}", "xdfl": "学前教育", "jbzlxList": ["教育部门"], "xdzl": "幼儿园", "jzglx": "专任教师"}
data4 = {"nd": f"{nd}", "xdfl": "学前教育", "jbzlxList": ["民办"], "xdzl": "幼儿园", "jzglx": "园长", "sfphxmbyey": "普惠"}
data5 = {"nd": f"{nd}", "xdfl": "学前教育", "jbzlxList": ["部队"], "xdzl": "幼儿园", "jzglx": "工勤人员"}
data6 = {"nd": f"{nd}", "xdfl": "学前教育", "cxlxList": ["城市"], "jbzlxList": ["教育部门"], "xdzl": "幼儿园", "jzglx": "专任教师"}
data7 = {"nd": f"{nd}", "xdfl": "学前教育", "cxlxList": ["城市"], "jbzlxList": ["民办"], "xdzl": "幼儿园", "jzglx": "专任教师",
         "sfphxmbyey": "普惠"}
data8 = {"nd": f"{nd}", "xdfl": "学前教育", "cxlxList": ["县镇"], "jbzlxList": ["民办"], "xdzl": "幼儿园", "jzglx": "园长",
         "sfphxmbyey": "普惠"}
data9 = {"nd": f"{nd}", "xdfl": "学前教育", "cxlxList": ["农村"], "xdzl": "幼儿园", "jzglx": "工勤人员"}
data10 = {"nd": f"{nd}", "xdfl": "学前教育", "cxlxList": ["农村"], "jbzlxList": ["民办"], "xdzl": "幼儿园", "jzglx": "工勤人员",
          "sfphxmbyey": "非普惠"}
data11 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "jzglx": "专任教师", "jzgxl": "博士研究生"}
data12 = {"nd": f"{nd}", "xdfl": "学前教育", "cxlxList": ["县镇"], "xdzl": "幼儿园", "jzglx": "园长", "jzgxl": "博士研究生"}
data13 = {"nd": f"{nd}", "xdfl": "学前教育", "cxlxList": ["农村"], "xdzl": "幼儿园", "jzglx": "园长", "jzgxl": "高中阶段"}
data14 = {"nd": f"{nd}", "xdfl": "学前教育", "xzqyList": ["东城区"], "xdzl": "幼儿园", "jzglx": "专任教师"}
data15 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "jzglx": "工勤人员", "sfzb": "在编人员"}
data16 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "jzglx": "行政人员", "sfzb": "在编人员"}
data17 = {"nd": "2023", "xdfl": "学前教育", "xdzl": "幼儿园", "jzglx": "教职工"}
data18 = {"nd": "2023", "xdfl": "学前教育", "xdzl": "幼儿园", "bxlxList": ["幼儿园"], "jzglx": "教职工"}
data19 = {"nd": f"{nd}", "xdfl": "学前教育", "xdzl": "幼儿园", "jzglx": "卫生保健人员", "sfzb": "在编人员"}

# 期望结果
num1 = 99987
num2 = 28166
num3 = 18522
num4 = 1184
num5 = 744
num6 = 14781
num7 = 12220
num8 = 106
num9 = 979
num10 = 46
num11 = 9
num12 = 1
num13 = 11
num14 = 2382
num15 = 850
num16 = 1333
num17 = 96381
num18 = 96381
num19 = 1302

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11, 12: data12, 13: data13, 14: data14, 15: data15, 16: data16, 17: data17, 18: data18, 19: data19}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11,
            12: num12, 13: num13, 14: num14, 15: num15, 16: num16, 17: num17, 18: num18, 19: num19}


# 执行方法
def test_teacher_api_yey():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_teacher_api_yey()
