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
import os
from scripts.handle_mysql import do_mysql
from scripts.handle_config import HandleConfig
from scripts.handle_register import do_register
from scripts.handle_path import CONFIG_USER_INFO_FILE_PATH


class HandleContext():
    """
    @staticmethod
    def judge_replace(pattern, repl, string):
    def judge_get(area_name, args, type=None):

    @classmethod
    def existed_tel(cls, data):
    def not_existed_tel(cls, data):
    def investors_user_tel(cls, data):
    def investors_user_pwd(cls, data):
    def manager_user_tel(cls, data):
    def manager_user_pwd(cls, data):
    def borrower_user_id(cls, data):
    def close(cls):
    """

    @staticmethod
    def judge_replace(pattern, repl, string):
        """
        判断是否存在模子，有将替换，无将返回原始字符串
        :param pattern: 需要被替换的模子（字符串）
        :param repl: 用来替换的字符串（do_mysql.existed_tel()）
        :param string: 原始字符串
        :return: data为被替换完的字符串；string为没有被替换的原始字符串
        """
        if re.search(pattern, string):
            data = re.sub(pattern, repl, string)
            return data
        else:
            return string

    @staticmethod
    def judge_get(area_name, args, type=None):
        """
        判断是否存在用户信息配置文件，有将获取对应值，可选择获取值得类型
        :param area_name:区域名
        :param args:区域项
        :param type:获取值类型方法
        :return:获取的值
        """
        while True:
            if os.path.exists(CONFIG_USER_INFO_FILE_PATH):
                if type == 'get_int':
                    area_value = HandleConfig(CONFIG_USER_INFO_FILE_PATH).get_int(area_name, args)
                elif type == 'get_float':
                    area_value = HandleConfig(CONFIG_USER_INFO_FILE_PATH).get_float(area_name, args)
                elif type == 'get_boolean':
                    area_value = HandleConfig(CONFIG_USER_INFO_FILE_PATH).get_boolean(area_name, args)
                elif type == 'get_eval_data':
                    area_value = HandleConfig(CONFIG_USER_INFO_FILE_PATH).get_eval_data(area_name, args)
                else:
                    area_value = HandleConfig(CONFIG_USER_INFO_FILE_PATH).get_value(area_name, args)
                return area_value
            else:
                do_register.write_config()

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
        context_data = cls.judge_replace(investors_user_tel_pattern, cls.judge_get('Investors', 'mobilephone'), data)
        return context_data

    @classmethod
    def investors_user_id(cls, data):
        investors_user_id_pattern = r'\${investors_user_id}'
        context_data = cls.judge_replace(investors_user_id_pattern, cls.judge_get('Investors', 'id'), data)
        return context_data

    @classmethod
    def investors_user_pwd(cls, data):
        investors_user_pwd_pattern = r'\${investors_user_pwd}'
        context_data = cls.judge_replace(investors_user_pwd_pattern, cls.judge_get('Investors', 'pwd'), data)
        return context_data

    @classmethod
    def not_existed_user_id(cls, data):
        not_existed_user_id_pattern = r'\${not_existed_user_id}'
        sql = 'SELECT MAX(Id) AS mid FROM member;'
        not_existed_user_id = str(do_mysql.run(sql=sql)["mid"] + 1)
        context_data = cls.judge_replace(not_existed_user_id_pattern, not_existed_user_id, data)
        return context_data

    @classmethod
    def manager_user_tel(cls, data):
        manager_user_tel_pattern = r'\${manager_user_tel}'
        context_data = cls.judge_replace(manager_user_tel_pattern, cls.judge_get('Manager', 'mobilephone'), data)
        return context_data

    @classmethod
    def manager_user_pwd(cls, data):
        manager_user_pwd_pattern = r'\${manager_user_pwd}'
        context_data = cls.judge_replace(manager_user_pwd_pattern, cls.judge_get('Manager', 'pwd'), data)
        return context_data

    @classmethod
    def borrower_user_id(cls, data):
        borrower_user_id_pattern = r'\${borrower_user_id}'
        context_data = cls.judge_replace(borrower_user_id_pattern, cls.judge_get('Borrower', 'id'), data)
        return context_data

    @classmethod
    def loan_id(cls, data):
        loan_id_pattern = r'\${loan_id}'
        if re.search(loan_id_pattern, data):
            loan_id_repl = str(getattr(cls, "loan_idw"))
            context_data = re.sub(loan_id_pattern, loan_id_repl, data)
            return context_data
        else:
            return data

    @classmethod
    def not_exitsed_loan_id(cls, data):
        not_exitsed_loan_id_pattern = r'\${not_existed_loan_id}'
        sql = "SELECT MAX(Id) AS total_loan_id FROM loan LIMIT 0, 1;"
        not_exitsed_loan_id = str(do_mysql.run(sql)["total_loan_id"] + 1)
        context_data = cls.judge_replace(not_exitsed_loan_id_pattern, not_exitsed_loan_id, data)
        return context_data

    @classmethod
    def close(cls):
        do_mysql.close()


if __name__ == '__main__':
    # one = HandleContext.not_existed_tel('{"mobilephone": "${not_existed_tel}", "pwd": 123456, "regname": "刀刀"}')
    # print(one)
    # two = HandleContext.existed_tel('{"mobilephone": "${existed_tel}", "pwd": 123456, "regname": "刀刀"}')
    # print(two)
    # three = HandleContext.investors_user_pwd(
    #     HandleContext.investors_user_tel('{"mobilephone": "${investors_user_tel}", "pwd": "${investors_user_pwd}"}'))
    # print(three)
    # four = HandleContext.manager_user_pwd(
    #     HandleContext.manager_user_tel('{"mobilephone": "${manager_user_tel}", "pwd": "${manager_user_pwd}"}'))
    # print(four)
    # five = HandleContext.borrower_user_id(
    #     '{"memberId": "${borrower_user_id}", "title": "试试人品行不行，介个2W玩玩", "amount": 20000,"loanRate":12.0,"loanTerm":3,"loanDateTpye":0,"repaymemtWay":11,"biddingDays":5}')
    # print(five)
    four = HandleContext.not_exitsed_loan_id('{"loanId":${not_existed_loan_id},"amount":500}')
    print(four)
    HandleContext.close()
