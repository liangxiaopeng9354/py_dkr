# -*- coding: utf-8 -*-
# @Time    : 2024-8-27 11:24
# @Author  : liangxiaopeng
# @File    : login_api.py

import http.client
import json

login_ip = '192.168.10.6'
user_name = 'yangya'
pswd = '123456'
login_url = '/api/auth/oauth2/token'
POST = 'POST'
uf_code = 'UTF-8'


def login_api():
    try:
        conn = http.client.HTTPConnection(login_ip)
        payload = f'client_id=test&client_secret=test&username={user_name}&password={pswd}&scope=server&grant_type=password'
        headers = {
            'Authorization': 'Basic dGVzdDp0ZXN0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        conn.request(POST, login_url, payload, headers)
        res = conn.getresponse()
        data = res.read()
        # 解码字节对象为字符串
        response_str = data.decode(uf_code)
        # 尝试将字符串解析为JSON对象
        response_dict = json.loads(response_str)
        # 现在可以安全地访问字典中的键了
        token_str = response_dict.get('access_token', 'Token type not found')
        # # 关闭连接
        conn.close()
        return token_str
    except http.client.HTTPException as e:
        print(f"HTTP error: {e}")
    except ConnectionRefusedError as e:
        print(f"Connection refused: {e}")
    except json.JSONDecodeError:
        print("Failed to decode JSON response")
