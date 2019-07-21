#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: handle_register.py
@Time: 2019-07-21 16:25
@Desc: S
"""
import re

from scripts.handle_config import do_config
from scripts.handle_mysql import do_mysql
from scripts.handle_path import CONFIG_USER_INFO_FILE_PATH
from scripts.handle_request import do_request


class HandleRegister:
    def __init__(self):
        self.pwd = 123456
        self.reg_name = '刀刀'

    # 1.使用程序生成未注册的手机号
    def not_existed_tel(self):
        not_existed_tel = do_mysql.not_existed_tel()
        print('数据库中不存在的手机号码为：{}'.format(not_existed_tel))
        return not_existed_tel

    # 2.使用程序注册3个账号：a.分别注册借款人、投资人、管理人账号
    def test_register(self):
        method = 'POST'
        url = do_config.get_value('request', 'default_address')
        path = '/member/register'
        data = {"mobilephone": "${not_existed_tel}", "pwd": self.pwd, "regname": self.reg_name}
        tel_list = []
        for i in range(3):
            not_existed_tel = str(self.not_existed_tel())
            tel_list.append(not_existed_tel)
            data_re = re.sub(r'\${not_existed_tel}', not_existed_tel, str(data))
            request_result = do_request.send_request(method, url=url + path, data=eval(data_re))
        do_request.request_close()
        return tel_list

    # 2.使用程序注册3个账号：b.需要获取每个账号的ID（数据库获取）、手机号、密码
    def get_user_info(self):
        user_info = []
        for j in self.test_register():
            search_result = do_mysql.sql_search(
                sql=('SELECT Id,RegName,MobilePhone,Pwd FROM member WHERE MobilePhone=%s'),
                virtue=j)
            user_info.append(search_result)
        return user_info

    # 2.使用程序注册3个账号：c.思考将这3个账号信息保存到哪里?
    def write_config(self):
        get_user_info = self.get_user_info()
        get_user_info_re = re.sub('E10ADC3949BA59ABBE56E057F20F883E', str(self.pwd), str(get_user_info))
        user_info_area_name = {'Borrower', 'Investors', 'Manager'}
        user_info = dict(zip(user_info_area_name, eval(get_user_info_re)))
        do_config.write_config(user_info, CONFIG_USER_INFO_FILE_PATH)

    def closs(self):
        do_mysql.close()


do_register = HandleRegister()

if __name__ == '__main__':
    my_register = HandleRegister()
    my_register.write_config()
    my_register.closs()
