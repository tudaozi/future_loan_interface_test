#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test.py
@Time: 2019/7/13 1:22
@Desc: S
"""
import json

from interface_automation.class_0709_mysql.cw_0709_config import do_config
from interface_automation.class_0709_mysql.cw_0709_request import do_request

# def create_tel():
#     tel_head = random.choice(['137', '138', '139'])
#     tel_tail = ''.join(random.sample(string.digits, 8))
#     full_tel = tel_head + tel_tail
#     return full_tel
#
#
# print(create_tel())
# def splice():
#     not_existed_tel = do_mysql.not_existed_tel(do_config.get_value('mysql', 'not_existed_tel'))
#     register_excel = HandleExcel(do_config.get_value('file path', 'case_path'), 'register')
#     register_excel_cases = register_excel.get_case()
#     register_excel_re = re.sub(r'\${not_existed_tel}', not_existed_tel, str(register_excel_cases))
#     existed_tel = do_mysql.existed_tel(do_config.get_value('mysql', 'existed_tel'),
#                                        do_config.get_int('mysql', 'existed_tel_type'))
#     register_cases = re.sub(r'\${existed_tel}', existed_tel, str(register_excel_re))
#     # register_cases = list(register_cases)
#     wb, ws = register_excel.load_excel()
#     wb.close()
#
#     return register_cases
#
#
# cases_list = splice()
# cases_list = eval(cases_list)
case_list = {'case_id': 1, 'title': '使用不存在的手机号进行注册', 'url_path': '/member/register',
             'data': '{"mobilephone": "13786245301", "pwd": 123456, "regname": "刀刀"}', 'method': 'POST',
             'expected': 'code: "10001",', 'actual': None, 'result': None}
# print(type(case_list),case_list)
method = case_list['method']
url = do_config.get_value('request', 'default_address') + case_list['url_path']
datas = case_list['data']
datas = eval(datas)

# actual = do_request.send_request(case_list['method'],
#                                         do_config.get_value('request', 'default_address') + case_list['url_path'],
#                                         eval(case_list['data']))

print(type(method), method)
print(type(url), url)
print(type(datas), datas)
# print(actual)


request_result = do_request.send_request(case_list['method'],
                                         do_config.get_value('request', 'default_address') + case_list['url_path'],
                                         case_list['data'])
actual_text = request_result.text
actual_value = json.loads(actual_text)['code']
actual = 'code: "{}",'.format(actual_value)
do_request.request_close()
result = case_list['expected']
msg = case_list['title']
print(actual)
