#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: test2.py
@Time: 2019-07-28 15:20
@Desc: S
"""
import unittest
from libs.ddt import ddt, data
from scripts.handle_config import do_config
from scripts.handle_mysql import do_mysql
from scripts.test_handle_excel import HandleExcel
from scripts.handle_log import do_logger
from scripts.handle_path import DATA_COMMON_FILE_PATH
from scripts.handle_request import do_request
from scripts.handle_context import HandleContext

my_excel = HandleExcel(DATA_COMMON_FILE_PATH, sheetname='invest')
cases_suite = my_excel.get_cases()


@ddt
class TestInvest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        do_logger.info('\n{:=^40s}\n'.format('开始执行用例'))

    @classmethod
    def tearDownClass(cls):
        my_excel.close_excel()
        do_request.request_close()
        do_logger.info('\n{:=^40s}\n'.format('用例执行结束'))

    @data(*cases_suite)
    def test_invest(self, case_list):
        case_list_str = str(case_list)
        context_data = HandleContext.manager_user_tel(case_list_str)
        context_data = HandleContext.manager_user_pwd(context_data)
        context_data = HandleContext.borrower_user_id(context_data)
        context_data = HandleContext.loan_id(context_data)
        context_data = HandleContext.investors_user_tel(context_data)
        context_data = HandleContext.investors_user_id(context_data)
        context_data = HandleContext.investors_user_pwd(context_data)
        context_data = HandleContext.not_existed_user_id(context_data)
        context_data = HandleContext.not_exitsed_loan_id(context_data)
        case_list_dict = eval(context_data)
        request_data = case_list_dict['data']
        method = case_list_dict['method']
        url = do_config.get_value('request', 'default_address') + case_list_dict['url_path']
        res = do_request.send_request(method, url, data=request_data)
        add_success_msg = do_config.get_value('request', 'add_success_msg')
        actual = res.text
        if add_success_msg in actual:
            check_sql = case_list_dict['check_sql']
            if check_sql:
                loan_id_sql = do_mysql.sql_search(check_sql)
                loan_id_value = loan_id_sql['Id']
                setattr(HandleContext, 'loan_idw', loan_id_value)
        result = str(case_list_dict['expected'])
        msg = case_list_dict['title']
        true_result = do_config.get_value('msg', 'true_result')
        fail_result = do_config.get_value('msg', 'fail_result')
        try:
            self.assertIn(result, actual, msg)
            print('{},执行结果为:{}'.format(msg, true_result))
            my_excel.write_result(case_list_dict['case_id'] + 1, actual, true_result)
            do_logger.error("{}, 执行结果为: {}".format(msg, true_result))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            my_excel.write_result(case_list_dict['case_id'] + 1, actual, fail_result)
            do_logger.error("{}, 执行结果为: {},具体异常为{}".format(msg, fail_result, e))
            raise e


if __name__ == '__main__':
    unittest.main()