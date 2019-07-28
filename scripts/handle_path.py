#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: handle_path.py
@Time: 2019/7/17 0:38
@Desc: 处理文件路径，供个模块调用
"""
import os


class HandlePath:
    """
    处理文件路径，供个模块调用
    """
    pass


# 获取根目录
# one_path=os.path.abspath(__file__)
# two_path=os.path.dirname(one_path)
# three_path=os.path.dirname(two_path)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取测试用例cases目录
CASES_DIR = os.path.join(BASE_DIR, 'cases')
CASES_TEST_01_REGISTER_FILE_PATH = os.path.join(CASES_DIR, 'test_01_register.py')
CASES_TEST_02_LOGIN_FILE_PATH = os.path.join(CASES_DIR, 'test_02_login.py')
CASES_TEST_03_RECHARGE_FILE_PATH = os.path.join(CASES_DIR, 'test_03_recharge.py')
CASES_TEST_04_ADD_FILE_PATH = os.path.join(CASES_DIR, 'test_04_add.py')
CASES_TEST_05_INVEST_FILE_PATH = os.path.join(CASES_DIR, 'test_05_invest.py')

# 获取配置文件config目录
CONFIG_DIR = os.path.join(BASE_DIR, 'config')
CONFIG_BASE_FILE_PATH = os.path.join(CONFIG_DIR, 'base.conf')
CONFIG_WRITE_CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, 'write_config.ini')
CONFIG_USER_INFO_FILE_PATH = os.path.join(CONFIG_DIR, 'user_info.conf')

# 获取测试数据data目录
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_COMMON_FILE_PATH = os.path.join(DATA_DIR, 'common.xlsx')
DATA_TEST_COMMON_FILE_PATH = os.path.join(DATA_DIR, 'test_common.xlsx')

# 获取第三方库文件libs目录
LIBS_DIR = os.path.join(BASE_DIR, 'libs')
LIBS_TEST_RUNNER_FILE_PATH = os.path.join(LIBS_DIR, 'HTMLTestRunnerNew.py')

# 获取日志文件logs目录
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
LOGS_DEBUG_FILE_PATH = os.path.join(LOGS_DIR, 'debug.log')
LOGS_INFO_FILE_PATH = os.path.join(LOGS_DIR, 'info.log')
LOGS_WARNING_FILE_PATH = os.path.join(LOGS_DIR, 'warning.log')
LOGS_ERROR_FILE_PATH = os.path.join(LOGS_DIR, 'error.log')
LOGS_CRITICAL_FILE_PATH = os.path.join(LOGS_DIR, 'critical.log')
LOGS_RUN_RECORD_FILE_PATH = os.path.join(LOGS_DIR, 'run_record.txt')

# 获取获取测试报告reports目录
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

# 获取脚本封装scripts目录
SCRIPTS_DIR = os.path.join(BASE_DIR, 'scripts')
HANDLE_CONFIG_FILE_PATH = os.path.join(SCRIPTS_DIR, 'handle_config.py')
HANDLE_CONTEXT_FILE_PATH = os.path.join(SCRIPTS_DIR, 'handle_context.py')
HANDLE_EXCEL_FILE_PATH = os.path.join(SCRIPTS_DIR, 'handle_excel.py')
HANDLE_TEST_EXCEL_FILE_PATH = os.path.join(SCRIPTS_DIR, 'test_handle_excel.py')
HANDLE_LOG_FILE_PATH = os.path.join(SCRIPTS_DIR, 'handle_log.py')
HANDLE_MYSQL_FILE_PATH = os.path.join(SCRIPTS_DIR, 'handle_mysql.py')
HANDLE_REQUEST_FILE_PATH = os.path.join(SCRIPTS_DIR, 'handle_request.py')
HANDLE_TEST_SUITE_FILE_PATH = os.path.join(SCRIPTS_DIR, 'handle_test_suite.py')

# 获取临时测试test目录
TEST_DIR = os.path.join(BASE_DIR, 'test')

pass
