#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: test2.py
@Time: 2019-07-28 23:37
@Desc: S
"""


# from test.test1 import test222
class Test2:
    @classmethod
    def test22(cls):
        test222 = getattr(cls, "test222")
        print(test222)
        return test222


Test2.test22()
