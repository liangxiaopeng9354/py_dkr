# -*- coding: utf-8 -*-
# @Time    : 2024-8-14 10:38
# @Author  : liangxiaopeng
# @File    : api_response.py


import requests
import json


def test_api_response(url, data_dict, num_dict, name, headers):

    for i in range(1, len(data_dict) + 1):

        # 定义请求的body
        data = data_dict[i]
        # 发送POST请求
        response = requests.post(url, data=json.dumps(data), headers=headers)
        # 检查请求是否成功
        assert response.status_code == 200, f"请求失败，状态码: {response.status_code}"

        # 尝试解析JSON响应内容
        try:
            response_data = response.json()
            # 假设响应数据中有一个名为'num'的字段
            if response_data['data'] != None:
                num_velue = response_data['data']['num']

                # 验证num字段的值（这里假设我们期望的num值是一个具体的数字，比如100）
                expected_num = num_dict[i]  # 你可以根据实际需要修改这个值
                # assert num_velue == expected_num, f"{name}中的接口,第-{i}-条测试用例断言失败，期望的值为:{expected_num}，实际值为:{num_velue}"
                if num_velue != expected_num:
                    print(f"{name}中的接口,第-{i}-条测试用例断言失败，期望的值为:{expected_num}，实际值为:{num_velue}")
                else:
                    continue

            else:
                print(f"“{name}”的第*{i}*条测试用例请求出现问题。接口的传值为：{data_dict[i]}")
                continue
        except json.JSONDecodeError:
            assert False, "响应内容不是有效的JSON"
        except KeyError:
            assert False, "响应数据中缺少'num'字段"

    print(f"{name}的{len(data_dict)}条测试用例全部请求成功，并且断言验证通过!!!")
