#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: test1.py
@Time: 2019-07-28 23:37
@Desc: S
"""
import random
import string
from test.test2 import Context
from scripts.handle_request import do_request
from scripts.handle_config import do_config
from scripts.handle_mysql import do_mysql


class ApiTest:
    for i in range(3):
        method = 'post'
        url = do_config.get_value('request', 'default_address') + '/member/register'
        data = '{"mobilephone": "${not_existed_tel}", "pwd": 123456, "regname": "刀刀"}'
        setattr(Context, 'existed', do_mysql.not_existed_tel())
        request_data = Context.mobilephone(data)
        res = do_request.send_request(method, url, data=request_data)
        print(res.text)
