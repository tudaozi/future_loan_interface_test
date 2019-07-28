#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: cw_0709_mysql.py
@Time: 2019-07-11 00:26
@Desc: S
"""

import random
import string
import pymysql
from scripts.handle_config import do_config


class HandleMySQL:
    def __init__(self):
        self.conn = pymysql.connect(
            host=do_config.get_value('mysql', 'host'),
            user=do_config.get_value('mysql', 'user'),
            password=do_config.get_value('mysql', 'password'),
            db=do_config.get_value('mysql', 'db'),
            port=do_config.get_int('mysql', 'port'),
            charset=do_config.get_value('mysql', 'charset'),
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def run(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    # 随机创建一个手机号码
    @staticmethod
    def create_tel():
        tel_head = random.choice(['131', '132', '133', '134', '135', '136', '137', '138', '139'])
        tel_tail = ''.join(random.sample(string.digits, 8))
        full_tel = tel_head + tel_tail
        return full_tel

    # 返回一个数据库中的手机号码
    def existed_tel(self, type=1):
        sql = 'SELECT MobilePhone FROM member WHERE Type=%s LIMIT 0,1;'
        existed_tel = self.run(sql=sql, args=((type),))
        if existed_tel:
            return existed_tel['MobilePhone']
        else:
            return '数据库中没有该类型的手机号码'

    # 创建一个数据库中没有的手机号码
    def not_existed_tel(self):
        sql = 'SELECT MobilePhone FROM member WHERE MobilePhone=%s;'
        while True:
            full_tel = self.create_tel()
            if not self.run(sql=sql, args=(full_tel), ):
                return full_tel

    # SQL查询
    def sql_search(self, sql, virtue=None):
        search_result = self.run(sql=sql, args=(virtue), )
        if search_result:
            return search_result
        else:
            return '你查询的数据不存在'

    def close(self):
        self.cursor.close()
        self.conn.close()


do_mysql = HandleMySQL()

if __name__ == '__main__':
    # user_type = 2
    # not_existed_tel = do_mysql.not_existed_tel()
    # print('数据库中不存在的手机号码为：{}'.format(not_existed_tel))
    # existed_tel = do_mysql.existed_tel()
    # print('数据库中已存在的手机号码为：{}'.format(existed_tel))
    sql = 'SELECT Id FROM future.loan WHERE MemberID=97 ORDER BY CreateTime DESC LIMIT 0,1'
    my_sql = do_mysql.sql_search(sql)
    do_mysql.close()
