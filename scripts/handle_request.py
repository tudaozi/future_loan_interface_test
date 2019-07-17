#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: cw_0706_request.py
@Time: 2019-07-08 01:01
@Desc: S
"""
import json

import requests

from scripts.handle_log import do_logger


class HttpRequest:
    def __init__(self):
        self.one_session = requests.Session()

    def send_request(self, method, url, data=None, is_json=False, **kwargs):
        method = method.upper()
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                do_logger.error("将json转为Python中的数据类型时, 出现异常: {}".format(e))
                data = eval(data)
        if method == 'GET':
            res = self.one_session.request(method=method, url=url, params=data, **kwargs)
        elif method == 'POST':
            if is_json:
                res = self.one_session.request(method=method, url=url, json=data, **kwargs)
            else:
                res = self.one_session.request(method=method, url=url, data=data, **kwargs)
        else:
            res = None
            do_logger.error("不支持【{}】方法请求".format(method))
        return res

    def request_close(self):
        self.one_session.close()


do_request = HttpRequest()

if __name__ == '__main__':
    url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/register'
    params = {
        'mobilephone': 13798288888,
        'pwd': 123456,
        'regname': '刀刀'
    }
    my_httprequest = HttpRequest()
    my_httprequest.send_request(method='GET', url=url, data=params)
