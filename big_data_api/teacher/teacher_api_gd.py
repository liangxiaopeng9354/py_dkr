# -*- coding: utf-8 -*-
# @Time    : 2024-8-15 15:20
# @Author  : liangxiaopeng
# @File    : teacher_api_gd.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "高等教育老师"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtgx/teacher/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "教职工"}
data2 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "专任教师"}
data3 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "专任教师", "zyjszw": "正高级"}
data4 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "专任教师", "jzgxl": "博士研究生"}
data5 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "校外教师", "zyjszw": "正高级"}
data6 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "专任教师", "nlfd": "45-49岁"}
data7 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "专任教师", "zyjszw": "正高级", "nlfd": "45-49岁"}
data8 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "专任教师", "nlfd": "40-44岁", "jzgxl": "博士研究生"}
data9 = {"nd": f"{nd}", "xdfl": "高等教育", "cxlxList": ["城市", "县镇", "农村", "其他"], "xdzl": "大学", "jzglx": "专任教师"}
data10 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "专任教师", "zyjszw": "未定职级", "nlfd": "65岁以上"}
data11 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "专任教师", "nlfd": "65岁以上"}
data12 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "专任教师", "zyjszw": "正高级", "nlfd": "65岁以上"}
data13 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jzglx": "专任教师", "nlfd": "65岁以上", "jzgxl": "博士研究生"}
data14 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学",
          "bxlxList": ["高等职业学校", "高等专科学校", "独立学院", "学院", "大学", "其他普通高教机构：分校、大专班", "培养研究生的科研机构"], "jzglx": "教职工"}

# 期望结果
num1 = 158136
num2 = 75381
num3 = 21938
num4 = 53516
num5 = 3387
num6 = 12246
num7 = 4192
num8 = 10068
num9 = 75381
num10 = 5
num11 = 528
num12 = 518
num13 = 383
num14 = 158136

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11, 12: data12, 13: data13, 14: data14}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11,
            12: num12, 13: num13, 14: num14}


# 执行方法
def test_teacher_api_gd():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_teacher_api_gd()
