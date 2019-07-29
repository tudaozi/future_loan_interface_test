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

import re


class Context:
    @classmethod
    def mobilephone(cls, data):
        pattern = r'\${not_existed_tel}'
        repl = getattr(cls, 'existed')
        string = data
        if re.search(pattern, string):
            new_data = re.sub(pattern, repl, string)
            return new_data
        else:
            return string
