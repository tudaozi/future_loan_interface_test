#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: handle_context.py
@Time: 2019/7/17 0:36
@Desc: S
"""
import re
from scripts.handle_mysql import do_mysql


class HandleContext():

    @staticmethod
    def judge_replace(pattern, repl, string):
        """

        :param pattern: 需要被替换的模子（字符串）
        :param repl: 用来替换的字符串（do_mysql.existed_tel()）
        :param string: 原始字符串
        :return: data为被替换完的字符串；string为没有被替换的原始字符串
        """
        if re.search(pattern, string):
            data = re.sub(pattern, repl, string)
            do_mysql.close()
            return data
        else:
            return string

    @classmethod
    def existed_tel(cls, data):
        existed_tel_pattern = r'\${existed_tel}'
        context_data = cls.judge_replace(existed_tel_pattern, do_mysql.existed_tel(), data)
        return context_data

    @classmethod
    def not_existed_tel(cls, data):
        not_existed_tel_pattern = r'\${not_existed_tel}'
        context_data = cls.judge_replace(not_existed_tel_pattern, do_mysql.not_existed_tel(), data)
        return context_data

    @classmethod
    def investors_user_tel(cls, data):
        investors_user_tel_pattern = r'\${investors_user_tel}'
        context_data = cls.judge_replace(investors_user_tel_pattern, do_mysql.investors_user_tel(), data)
        return context_data

    @classmethod
    def investors_user_pwd(cls, data):
        investors_user_pwd_pattern = r'\${investors_user_pwd}'
        context_data = cls.judge_replace(investors_user_pwd_pattern, do_mysql.existed_tel(), data)
        return context_data

    @classmethod
    def manager_user_tel(cls, data):
        manager_user_tel_pattern = r'\${manager_user_tel}'
        context_data = cls.judge_replace(manager_user_tel_pattern, do_mysql.existed_tel(), data)
        return context_data

    @classmethod
    def manager_user_pwd(cls, data):
        manager_user_pwd_pattern = r'\${manager_user_pwd}'
        context_data = cls.judge_replace(manager_user_pwd_pattern, do_mysql.existed_tel(), data)
        return context_data

    @classmethod
    def borrower_user_id(cls, data):
        borrower_user_id_pattern = '${borrower_user_id}'
        context_data = cls.judge_replace(borrower_user_id_pattern, do_mysql.existed_tel(), data)
        return context_data


if __name__ == '__main__':
    tel = HandleContext.existed_tel('{"mobilephone": "${not_existed_tel}", "pwd": 123456, "regname": "刀刀"}')
    print(tel)
    tel_two = HandleContext.existed_tel('{"mobilephone": "${existed_tel}", "pwd": 123456, "regname": "刀刀"}')
    print(tel_two)
