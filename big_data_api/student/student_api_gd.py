# -*- coding: utf-8 -*-
# @Time    : 2024-8-14 10:38
# @Author  : liangxiaopeng
# @File    : student_api_gd.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "高等教育学生"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtgx/student/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "在校生", "jylx": "普通本科"}
data2 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "招生", "jylx": "普通本科"}
data3 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "毕业生", "jylx": "普通本科"}
data4 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "毕业生", "jylx": "成人专科"}
data5 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "招生", "jylx": "成人专科"}
data6 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "在校生", "jylx": "成人专科"}
data7 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "在校生", "jylx": "成人本科"}
data8 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "招生", "jylx": "成人本科"}
data9 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "毕业生", "jylx": "成人本科"}
data10 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "在校生", "jylx": "硕士研究生"}
data11 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "招生", "jylx": "硕士研究生"}
data12 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "毕业生", "jylx": "硕士研究生"}
data13 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "毕业生", "jylx": "博士研究生"}
data14 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "在校生", "jylx": "博士研究生"}
data15 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "招生", "jylx": "博士研究生"}
data16 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "毕业生", "jylx": "成人专科"}
data17 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "在校生", "jylx": "成人专科"}
data18 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "招生", "jylx": "成人专科"}
data19 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "毕业生", "jylx": "成人本科"}
data20 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "在校生", "jylx": "成人本科"}
data21 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "招生", "jylx": "成人本科"}
data22 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "毕业生", "jylx": "网络专科"}
data23 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "毕业生", "jylx": "网络本科"}
data24 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "bxlxList": ["独立学院"], "zbz": "在校生", "jylx": "普通本科"}
data25 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jbzlxList": ["教育部门"], "zbz": "毕业生", "jylx": "成人专科"}
data26 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jbzlxList": ["教育部门"], "zbz": "在校生", "jylx": "成人专科"}
data27 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "cxlxList": ["城市", "县镇", "农村", "其他"], "zbz": "在校生"}
data28 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "jbzlxList": ["教育部门", "其他部门", "民办"], "zbz": "招生", "jylx": "普通本科"}
data29 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "在校生", "gjxstzjk": "优秀"}
data30 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "bxlxList": ["高等职业学校"], "zbz": "在校生", "jylx": "职业专科"}
data31 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "招生", "jylx": "网络本科"}
data32 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学", "zbz": "在校生"}
data33 = {"nd": f"{nd}", "xdfl": "高等教育", "xdzl": "大学",
          "bxlxList": ["大学", "学院", "独立学院", "高等专科学校", "高等职业学校", "其他普通高教机构：分校、大专班", "培养研究生的科研机构"], "zbz": "在校生"}

# 期望结果
num1 = 535113
num2 = 139694
num3 = 127393
num4 = 5610
num5 = 2800
num6 = 5730
num7 = 68843
num8 = 25207
num9 = 30401
num10 = 294614
num11 = 109213
num12 = 89569
num13 = 19125
num14 = 117416
num15 = 29032
num16 = 5610
num17 = 5730
num18 = 2800
num19 = 30401
num20 = 68843
num21 = 25207
num22 = 92508
num23 = 155360
num24 = 19860
num25 = 2781
num26 = 2554
num27 = 1654803
num28 = 139694
num29 = 12008
num30 = 54729
num31 = 158296
num32 = 1654803
num33 = 1654803

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11, 12: data12, 13: data13, 14: data14, 15: data15, 16: data16, 17: data17, 18: data18, 19: data19,
             20: data20, 21: data21, 22: data22, 23: data23, 24: data24, 25: data25, 26: data26, 27: data27, 28: data28,
             29: data29, 30: data30, 31: data31, 32: data32, 33: data33}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11,
            12: num12, 13: num13, 14: num14, 15: num15, 16: num16, 17: num17, 18: num18, 19: num19, 20: num20,
            21: num21, 22: num22, 23: num23, 24: num24, 25: num25, 26: num26, 27: num27, 28: num28, 29: num29,
            30: num30, 31: num31, 32: num32, 33: num33}


# 执行方法
def test_student_api_gd():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_student_api_gd()
