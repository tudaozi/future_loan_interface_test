#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: run.py
@Time: 2019/7/17 0:09
@Desc: S
"""
import os
import unittest
from datetime import datetime
from libs import HTMLTestRunnerNew
from scripts.handle_path import REPORTS_DIR
from scripts.handle_path import CASES_DIR

suite = unittest.defaultTestLoader.discover(CASES_DIR)

report_name_prefix = 'test_reports_'
report_name_suffix = '.html'
report_name_time = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')
report_name = report_name_prefix + report_name_time + report_name_suffix
report_path = os.path.join(REPORTS_DIR, report_name)
with open(report_path, 'wb')as save_file:
    result = HTMLTestRunnerNew.HTMLTestRunner(stream=save_file, verbosity=2, title='前程贷实战测试报告_' + report_name_time,
                                              description='前程贷实战测试报告_' + report_name_time,
                                              tester='刀刀')
    result.run(suite)
