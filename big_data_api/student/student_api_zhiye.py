# -*- coding: utf-8 -*-
# @Time    : 2024-8-14 10:38
# @Author  : liangxiaopeng
# @File    : student_api_zhiye.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "***职业教育学生-2022年缺少附设中职班"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtzz/student/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "zbz": "在校生"}  # 在校生
data2 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "zbz": "招生"}  # 招生
data3 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "zbz": "毕业生"}  # 招生
data4 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校", "成人中等专业学校", "职业高中学校"], "zbz": "在校生"}
data5 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"], "zbz": "在校生"}
data6 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["成人中等专业学校"], "zbz": "毕业生"}
data7 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"], "zbz": "毕业生", "sfqrz": "全日制"}
data8 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["职业高中学校"], "zbz": "在校生", "sfqrz": "非全日制"}
data9 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "jbzlxList": ["地方企业"], "zbz": "在校生"}
data10 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "zbz": "毕业生", "sfqrz": "全日制"}
data11 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "jbzlxList": ["教育部门"], "zbz": "在校生", "sfqrz": "非全日制"}
data12 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "zbz": "在校生", "nj": "一年级"}
data13 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "zbz": "在校生", "nj": "一年级", "sfqrz": "非全日制"}
data14 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "zbz": "在校生", "nlfd": "14岁以下,15岁,16岁,17岁,18岁,19岁,20岁,21岁,22岁以上"}
data15 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "zbz": "在校生", "gjxstzjk": "优秀"}

# 期望结果
num1 = 39635
num2 = 14559
num3 = 8280
num4 = 39635
num5 = 20055
num6 = 779
num7 = 4092
num8 = 1554
num9 = 704
num10 = 7187
num11 = 1554
num12 = 14582
num13 = 1264
num14 = 39635
num15 = 1750

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11, 12: data12, 13: data13, 14: data14, 15: data15}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11,
            12: num12, 13: num13, 14: num14, 15: num15}


# 执行方法
def test_student_api_zhiye():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_student_api_zhiye()
