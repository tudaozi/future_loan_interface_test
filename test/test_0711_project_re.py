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
from scripts.handle_path import CONFIG_USER_INFO_FILE_PATH
from scripts.handle_request import do_request


class ClassWork:
    def __init__(self):
        self.pwd = 123456
        self.reg_name = '刀刀'

    # 1.使用程序生成未注册的手机号
    def not_existed_tel(self):
        not_existed_tel = do_mysql.not_existed_tel('SELECT MobilePhone FROM member WHERE MobilePhone=%s;')
        print('数据库中不存在的手机号码为：{}'.format(not_existed_tel))
        return not_existed_tel

    # 2.使用程序注册3个账号
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

    def get_user_info(self):
        user_infos = []
        for j in self.test_register():
            user_info = do_mysql.user_info(sql=('SELECT Id,MobilePhone FROM member WHERE MobilePhone=%s'),
                                           virtue=j)
            user_infos.append(user_info)
        return user_infos

    def write_config(self, ):
        get_user_info = self.get_user_info()
        user_info_area_name = ['Borrower', 'Investors', 'Manager']
        user_info = {}
        for k in get_user_info:
            user_id, mobile_phone = k['Id'], k['MobilePhone']
        for l in user_info_area_name:
            user_info.update({
                l: {
                    'user_id': user_id,
                    'reg_name': self.reg_name,
                    'mobile_phone': mobile_phone,
                    'pwd': self.pwd}
            })
        do_config.write_config(user_info, CONFIG_USER_INFO_FILE_PATH)


if __name__ == '__main__':
    my_classwork = ClassWork()
    # my_classwork.test_register()
    # my_classwork.get_user_info()
    my_classwork.write_config()
    do_mysql.close()
