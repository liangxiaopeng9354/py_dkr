# -*- coding: utf-8 -*-
# @Time    : 2024-8-19 10:38
# @Author  : liangxiaopeng
# @File    : shouye_api_stu.py

from tool.api_dic import *
from tool.api_response_tool import test_api_response

name = "首页学生接口"
# 定义API URL
url = f'{ip}api/sjfx/itemData/gtxd/student/summaryInfo'
headers = HEADERS # 设置请求头为JSON
# 定义请求body
# 学生
data1 = {"nd":f"{synd}","xdfl":"学前教育","zbz":"招生"}
data2 = {"nd":f"{synd}","xdfl":"学前教育","zbz":"毕业生"}
data3 = {"nd":f"{synd}","xdfl":"学前教育","zbz":"在校生"}
data4 = {"nd":f"{synd}","xdfl":"基础教育","zbz":"招生"}
data5 = {"nd":f"{synd}","xdfl":"基础教育","zbz":"毕业生"}
data6 = {"nd":f"{synd}","xdfl":"基础教育","zbz":"在校生"}
data7 = {"nd":f"{synd}","xdfl":"职业教育","zbz":"招生"}
data8 = {"nd":f"{synd}","xdfl":"职业教育","zbz":"毕业生"}
data9 = {"nd":f"{synd}","xdfl":"职业教育","zbz":"在校生"}
data10 = {"nd":f"{synd}","xdfl":"高等教育","zbz":"招生"}
data11 = {"nd":f"{synd}","xdfl":"高等教育","zbz":"毕业生"}
data12 = {"nd":f"{synd}","xdfl":"高等教育","zbz":"在校生"}


# 期望结果
num1 = 164082
num2 = 208037
num3 = 515267
num4 = 449954
num5 = 315803
num6 = 1749608
num7 = 20637
num8 = 15527
num9 = 58508
num10 = 370198
num11 = 444841
num12 = 1549925


data_dict = {1: data1, 2: data2, 3: data3, 4: data4, 5: data5, 6: data6, 7: data7, 8: data8, 9: data9, 10: data10,
             11: data11, 12: data12}
num_dict = {1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8, 9: num9, 10: num10, 11: num11,
            12: num12}


# 执行方法
def test_shouye_api_stu():
    test_api_response(url, data_dict, num_dict, name, headers)


if __name__ == '__main__':
    test_shouye_api_stu()
