# -*- coding: utf-8 -*-
# @Time    : 2024-8-16 9:38
# @Author  : liangxiaopeng
# @File    : teacher_api_xx.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "小学老师"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtxx/teacher/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "jzglx": "专任教师", "jzgxl": "博士研究生"}
data2 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "jzglx": "专任教师", "jzgxl": "专科毕业"}
data3 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "jzglx": "专任教师", "zyjszw": "正高级"}
data4 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "jzglx": "专任教师", "zyjszw": "正高级", "nlfd": "50-54岁"}
data5 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "jzglx": "专任教师", "zyjszw": "员级", "nlfd": "35-39岁"}
data6 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "jzglx": "专任教师", "zyjszw": "中级", "nlfd": "35-39岁"}
data7 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "jzglx": "专任教师", "zyjszw": "助理级", "nlfd": "35-39岁"}
data8 = {"nd": f"{nd}", "xdfl": "基础教育", "cxlxList": ["城市", "县镇", "农村", "其他"], "xdzl": "普通小学", "jzglx": "专任教师"}
data9 = {"nd": f"{nd}", "xdfl": "基础教育", "xzqyList": ["东城区"], "xdzl": "普通小学", "jzglx": "专任教师"}
data10 = {"nd": f"{nd}", "xdfl": "基础教育", "cxlxList": ["县镇"], "xdzl": "普通小学", "jzglx": "校外教师"}
data11 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "jzglx": "专任教师"}
data12 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "jzglx": "教职工"}
data13 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通小学", "bxlxList": ["小学"], "jzglx": "教职工"}

# 期望结果
num1 = 67
num2 = 2934
num3 = 87
num4 = 40
num5 = 92
num6 = 4691
num7 = 3918
num8 = 60484
num9 = 5422
num10 = 3
num11 = 60484
num12 = 66748
num13 = 66748

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11, 12: data12, 13: data13}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11,
            12: num12, 13: num13}


# 执行方法
def test_teacher_api_xx():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_teacher_api_xx()
