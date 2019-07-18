#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0629_handle_config.py
@Time: 2019-07-05 01:48
@Desc: 封装配置文件
"""
from configparser import ConfigParser

from scripts.handle_path import CONFIG_BASE_FILE_PATH
from scripts.handle_path import CONFIG_WRITE_CONFIG_FILE_PATH


class HandleConfig:  # 新建config封装类
    """
    封装配置文件
    """

    def __init__(self, filename=None):
        self.filename = filename  # 设定配置文件名
        self.config = ConfigParser()  # 初始化对象
        self.config.read(self.filename, encoding='utf-8')  # 读取指定配置文件

    def get_value(self, section, option):
        """

        :param section:
        :param option:
        :return:
        """
        return self.config.get(section, option)

    def get_int(self, section, option):
        """

        :param section:
        :param option:
        :return:
        """
        return self.config.getint(section, option)

    def get_float(self, section, option):
        """

        :param section:
        :param option:
        :return:
        """
        return self.config.getfloat(section, option)

    def get_boolean(self, section, option):
        """

        :param section:
        :param option:
        :return:
        """
        return self.config.getboolean(section, option)

    def get_eval_data(self, section, option):
        """

        :param section:
        :param option:
        :return:
        """
        return eval(self.get_value(section, option))

    @staticmethod
    def write_config(data, filename):
        """

        :param data:
        :param filename:
        :return:
        """
        config = ConfigParser()
        for key in data:
            config[key] = data[key]

        # 3. 保存到文件
        with open(filename, 'w') as file:
            config.write(file)


do_config = HandleConfig(CONFIG_BASE_FILE_PATH)

if __name__ == '__main__':
    data_info = {
        "file path": {'cases_path': 'DATA_COMMON_FILE_PATH', 'log_path': 'LOGS_RUN_RECORD_FILE_PATH'},
        "msg": {'success_result': 'Pass', 'fail_result': 'Fail'}
    }
    write_filename = CONFIG_WRITE_CONFIG_FILE_PATH
    # HandleConfig.write_config(data_info, write_filename)
    do_config.write_config(data_info, write_filename)
    pass
