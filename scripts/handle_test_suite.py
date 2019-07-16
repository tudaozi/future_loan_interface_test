#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0625_case_suite_1.py
@Time: 2019-06-29 22:19
@Desc: S
"""
import unittest

from scripts.handle_path import CASES_DIR

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(CASES_DIR.ApiTest))

if __name__ == '__main__':
    unittest.main()
