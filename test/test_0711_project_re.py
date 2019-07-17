#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: test_0711_project_re.py
@Time: 2019-07-18 00:35
@Desc: S
"""
import re

from scripts.handle_config import do_config
from scripts.handle_mysql import do_mysql
from scripts.handle_request import do_request


class ClassWork:
    # 1.使用程序生成未注册的手机号
    def not_existed_tel(self):
        not_existed_tel = do_mysql.not_existed_tel('SELECT MobilePhone FROM member WHERE MobilePhone=%s;')
        # print('数据库中不存在的手机号码为：{}'.format(not_existed_tel))
        # do_mysql.close()
        return not_existed_tel

    # 2.使用程序注册3个账号
    def test_register(self):
        method = 'POST'
        url = do_config.get_value('request', 'default_address')
        path = '/member/register'
        data = {"mobilephone": "${not_existed_tel}", "pwd": 123456, "regname": "刀刀"}
        not_existed_tel = self.not_existed_tel()
        data_re = re.sub(r'\${not_existed_tel}', not_existed_tel, str(data))

        request_result = do_request.send_request(method, url=url + path, data=eval(data_re))
        do_request.request_close()
        # print(not_existed_tel)
        return not_existed_tel

    def get_user_info(self):
        not_existed_tel = self.test_register()
        user_info = do_mysql.user_info(sql=('SELECT Id,RegName,MobilePhone,Pwd FROM member WHERE MobilePhone=%s'),
                                       virtue=not_existed_tel)
        print(user_info)
        return user_info

    def write_config(self):
        user_info = {
            user_info: {
                'id' =
        }
        }
        do_config.write_config()


my_classwork = ClassWork()
# my_classwork.test_register()
my_classwork.get_user_info()
do_mysql.close()
