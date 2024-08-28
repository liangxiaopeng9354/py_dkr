# -*- coding: utf-8 -*-
# @Time    : 2024-8-27 11:24
# @Author  : liangxiaopeng
# @File    : login_api_new.py

import requests

login_url = 'http://192.168.10.6/api/auth/oauth2/token'
user_name = 'yangya'
pswd = '123456'
headers = {
    'Authorization': 'Basic dGVzdDp0ZXN0',
    'Content-Type': 'application/x-www-form-urlencoded'
}
payload = {
    'client_id': 'test',
    'client_secret': 'test',
    'username': user_name,
    'password': pswd,
    'scope': 'server',
    'grant_type': 'password'
}


def login_api():
    try:
        response = requests.post(login_url, data=payload, headers=headers)
        response.raise_for_status()  # 如果响应状态码不是200系列，将抛出HTTPError
        return response.json().get('access_token', 'Token not found')
    except requests.RequestException as e:
        return str(e)


if __name__ == '__main__':
    print(login_api())
