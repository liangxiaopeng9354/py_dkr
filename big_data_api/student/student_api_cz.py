# -*- coding: utf-8 -*-
# @Time    : 2024-8-19 10:38
# @Author  : liangxiaopeng
# @File    : school_api_cz.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "普通教育初中生"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtcz/student/summaryInfo'
headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "zbz": "在校生"}  # 在校生
data2 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "zbz": "招生"}  # 招生
data3 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "zbz": "毕业生"}  # 招生
data4 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "xzqyList": ["东城区"], "zbz": "在校生"}
data5 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "cxlxList": ["城市"], "zbz": "在校生"}
data6 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "cxlxList": ["城市", "县镇", "农村", "其他"], "zbz": "在校生"}
data7 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "cxlxList": ["农村"], "jbzlxList": ["民办"], "zbz": "在校生"}
data8 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "cxlxList": ["县镇"], "jbzlxList": ["民办"], "zbz": "毕业生"}
data9 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "jbzlxList": ["地方企业"], "zbz": "在校生"}
data10 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "zbz": "在校生", "zjz": "寄宿生"}
data11 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "zbz": "在校生", "zjz": "进城务工人员随迁子女"}
data12 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "cxlxList": ["农村"], "zbz": "在校生"}
data13 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "zbz": "在校生", "sfgjxs": "国际学生"}
data14 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "bxlxList": ["九年一贯制学校", "初级中学", "附设普通初中班", "十二年一贯制学校", "完全中学"],
          "zbz": "在校生"}
data15 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "zbz": "在校生", "tjqk": "参加体检学生"}
data16 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "zbz": "在校生", "gjxstzjk": "优秀"}
data17 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "zbz": "在校生"}
data18 = {"nd": f"{nd}", "xdfl": "基础教育", "xdzl": "普通初中", "bxlxList": ["九年一贯制学校", "初级中学", "附设普通初中班", "十二年一贯制学校", "完全中学"],
          "zbz": "在校生"}

# 期望结果
num1 = 355820
num2 = 121270
num3 = 103514
num4 = 26579
num5 = 310466
num6 = 355820
num7 = 1424
num8 = 1580
num9 = 741
num10 = 29307
num11 = 16915
num12 = 18632
num13 = 538
num14 = 355820
num15 = 584489
num16 = 179211
num17 = 355820
num18 = 355820

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11, 12: data12, 13: data13, 14: data14, 15: data15, 16: data16, 17: data17, 18: data18}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11,
            12: num12, 13: num13, 14: num14, 15: num15, 16: num16, 17: num17, 18: num18}


# 执行方法
def test_student_api_cz():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_student_api_cz()
