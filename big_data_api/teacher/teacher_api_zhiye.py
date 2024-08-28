# -*- coding: utf-8 -*-
# @Time    : 2024-8-15 13:28
# @Author  : liangxiaopeng
# @File    : teacher_api_yey.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "***职业教育老师-缺少附设中职班"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtzz/teacher/summaryInfo'

headers = HEADERS  # 设置请求头为JSON
# 定义请求body
data1 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "jzglx": "教职工"}
data2 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校", "成人中等专业学校", "职业高中学校"], "jzglx": "教职工"}
data3 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["成人中等专业学校"], "jzglx": "教辅人员"}
data4 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"], "jzglx": "专任教师", "zyjszw": "正高级"}
data5 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"], "jzglx": "校外教师"}
data6 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["职业高中学校"], "jzglx": "专任教师", "zyjszw": "初级"}
data7 = {"nd": f"{nd}", "xdfl": "职业教育", "jbzlxList": ["地方企业"], "xdzl": "中职", "jzglx": "专任教师", "zyjszw": "正高级"}
data8 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"], "jzglx": "专任教师", "nlfd": "29岁以下"}
data9 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["职业高中学校"], "jzglx": "专任教师", "nlfd": "45-49岁"}
data10 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "jzglx": "专任教师", "sfzb": "在编人员"}
data11 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["职业高中学校"], "jzglx": "教职工", "sfzb": "在编人员"}
data12 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["职业高中学校"], "jzglx": "专任教师", "bxnsfsk": "本学年授课"}
data13 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"], "jzglx": "校外教师", "bxnsfsk": "本学年授课"}
data14 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["职业高中学校"], "jzglx": "专任教师", "bxnsfsk": "本学年不授课"}
data15 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"], "jzglx": "专任教师", "jzgxl": "硕士研究生"}
data16 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["职业高中学校"], "jzglx": "专任教师", "jzgxl": "专科"}
data17 = {"nd": f"{nd}", "xdfl": "职业教育", "jbzlxList": ["民办"], "xdzl": "中职", "jzglx": "专任教师", "zyjszw": "初级"}
data18 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"], "jzglx": "专任教师", "zyjszw": "正高级",
          "bxnsfsk": "本学年授课"}
data19 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["中等技术学校"], "jzglx": "专任教师", "zyjszw": "中级",
          "bxnsfsk": "本学年授课"}
data20 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["成人中等专业学校"], "jzglx": "校外教师", "zyjszw": "中级",
          "jzgxl": "本科"}
data21 = {"nd": f"{nd}", "xdfl": "职业教育", "xdzl": "中职", "bxlxList": ["职业高中学校"], "jzglx": "专任教师", "zyjszw": "中级",
          "nlfd": "45-49岁"}

# 期望结果
num1 = 8390
num2 = 8390
num3 = 40
num4 = 46
num5 = 172
num6 = 673
num7 = 6
num8 = 123
num9 = 794
num10 = 5035
num11 = 4345
num12 = 3117
num13 = 155
num14 = 212
num15 = 488
num16 = 26
num17 = 41
num18 = 44
num19 = 616
num20 = 40
num21 = 338

data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11, 12: data12, 13: data13, 14: data14, 15: data15, 16: data16, 17: data17, 18: data18, 19: data19,
             20: data20, 21: data21}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11,
            12: num12, 13: num13, 14: num14, 15: num15, 16: num16, 17: num17, 18: num18, 19: num19, 20: num20,
            21: num21}


# 执行方法
def test_teacher_api_zhiye():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_teacher_api_zhiye()
