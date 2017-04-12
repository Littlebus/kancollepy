#! /usr/bin/python3

import getpass
import json
import requests

if __name__ == '__main__':
    user = input('username: ')
    passwd = getpass.getpass('password: ')
    post_data = {'username': user, 'password': passwd, 'iprange': 'yes'}
    url = 'https://its.pku.edu.cn/cas/webLogin'
    resp = requests.post(url, data=post_data)
    print(resp)
