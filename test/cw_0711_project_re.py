#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: cw_0711_project_re.py
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
        user_infos = []
        for j in self.test_register():
            user_info = do_mysql.user_info(sql=('SELECT Id,RegName,MobilePhone,Pwd FROM member WHERE MobilePhone=%s'),
                                           virtue=j)
            user_infos.append(user_info)
        return user_infos

    # 2.使用程序注册3个账号：c.思考将这3个账号信息保存到哪里?
    def write_config(self):
        get_user_info = self.get_user_info()
        get_user_info_re = re.sub('E10ADC3949BA59ABBE56E057F20F883E', str(self.pwd), str(get_user_info))
        user_info_area_name = {'Borrower', 'Investors', 'Manager'}
        user_info = dict(zip(user_info_area_name, eval(get_user_info_re)))
        do_config.write_config(user_info, CONFIG_USER_INFO_FILE_PATH)

    # 3.演练正则匹配操作
    @staticmethod
    def handle_re():
        pattern_string = 'a,b,c,d,e,f,g'
        match_result_true = re.match('a', pattern_string).span()
        match_result_false = re.match('b', pattern_string)
        search_result = re.search('c', pattern_string)
        sub_result = re.sub('d', 'pattern', pattern_string)
        return match_result_true, match_result_false, search_result, sub_result


if __name__ == '__main__':
    my_classwork = ClassWork()
    my_classwork.write_config()
    print(my_classwork.handle_re())
    do_mysql.close()
