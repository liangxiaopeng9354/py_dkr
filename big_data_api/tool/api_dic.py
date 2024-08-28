# -*- coding: utf-8 -*-
# @Time    : 2024-8-21 15:23
# @Author  : liangxiaopeng
# @File    : api_dic.py

from login_api_new import *

# 服务连接地址
ip = 'http://192.168.10.6/'
# 重新登录获取token
print(f"重新登录{user_name}获取token")
access_token = login_api()

# 组装请求头
HEADERS = {'Content-Type': 'application/json', 'authorization': f'Bearer {access_token}'}  # 设置请求头为JSON

# 年度
nd = 2022

# 首页年度
synd = 2023
