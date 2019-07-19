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

user_info_two = [{'Id': 104119, 'MobilePhone': '13710967842'}, {'Id': 104120, 'MobilePhone': '13873842506'},
                 {'Id': 104121, 'MobilePhone': '13934982715'}]

user_info_one = {'Borrower', 'Investors', 'Manager'}
user_info = dict(zip(user_info_one, user_info_two))
print(user_info)
