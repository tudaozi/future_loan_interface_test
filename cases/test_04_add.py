#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: test_04_add.py
@Time: 2019-07-21 23:31
@Desc: S
"""

import json
import unittest
from libs.ddt import ddt, data
from scripts.handle_config import do_config
from scripts.handle_mysql import do_mysql
from scripts.handle_excel import HandleExcel
from scripts.handle_log import do_logger
from scripts.handle_path import DATA_COMMON_FILE_PATH
from scripts.handle_request import do_request
from scripts.handle_context import HandleContext

true_result = do_config.get_value('msg', 'true_result')
fail_result = do_config.get_value('msg', 'fail_result')


def excel_suite():
    register_excel = HandleExcel(DATA_COMMON_FILE_PATH, 'add')  # 实例化对象
    register_excel_cases = register_excel.get_cases()  # 获取excel测试用例
    register_cases = HandleContext.borrower_user_id(
        HandleContext.manager_user_pwd(HandleContext.manager_user_tel(str(register_excel_cases))))  # 执行参数化替换
    register_cases = eval(register_cases)
    wb, ws = register_excel.load_excel()
    wb.close()
    return register_cases


cases_suite = excel_suite()


@ddt
class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        do_logger.info('\n{:=^40s}\n'.format('开始执行用例'))

    @classmethod
    def tearDownClass(cls):
        do_logger.info('\n{:=^40s}\n'.format('用例执行结束'))

    def setUp(self):
        pass

    def tearDown(self):
        wb, ws = self.my_HandleExcel.load_excel()
        wb.save(DATA_COMMON_FILE_PATH)
        wb.close()
        do_request.request_close()

    @data(*cases_suite)
    def test_add(self, case_list):
        self.my_HandleExcel = HandleExcel(DATA_COMMON_FILE_PATH, 'add')
        request_result = do_request.send_request(case_list['method'],
                                                 do_config.get_value('request', 'default_address') + case_list[
                                                     'url_path'],
                                                 case_list['data'])
        actual = int(request_result.json().get('code'))
        result = case_list['expected']
        msg = case_list['title']
        try:
            self.assertEqual(result, actual, msg)
            print('{},执行结果为:{}'.format(msg, true_result))
            self.my_HandleExcel.write_result(case_list['case_id'] + 1, actual, true_result)
            do_logger.error("{}, 执行结果为: {}".format(msg, true_result))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.my_HandleExcel.write_result(case_list['case_id'] + 1, actual, fail_result)
            do_logger.error("{}, 执行结果为: {},具体异常为{}".format(msg, fail_result, e))
            raise e


if __name__ == '__main__':
    unittest.main()
