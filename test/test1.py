#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: test1.py
@Time: 2019-07-28 23:37
@Desc: S
"""
from test.test2 import Test2


class Test1:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def test11(self):
        d = self.a + self.b + self.c
        setattr(Test2, "test222", 5)
        return d
