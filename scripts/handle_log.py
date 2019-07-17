#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0629_log.py
@Time: 2019-07-05 00:11
@Desc: S
"""

import logging

from scripts.handle_config import do_config
from scripts.handle_path import LOGS_DEBUG_FILE_PATH

logger_name = do_config.get_value('log', 'logger_name')
logger_level = do_config.get_value('log', 'logger_level')
console_leves = do_config.get_value('log', 'console_leves')
file_level = do_config.get_value('log', 'file_level')
simple_formatter_confing = do_config.get_value('log', 'simple_formatter')
verbose_formatter_config = do_config.get_value('log', 'verbose_formatter')


class HandleLog:
    def __init__(self):
        self.case_logger = logging.getLogger(logger_name)
        self.case_logger.setLevel(logger_level)

        console_handle = logging.StreamHandler()
        file_handle = logging.FileHandler(LOGS_DEBUG_FILE_PATH, encoding='utf-8')

        console_handle.setLevel(console_leves)
        file_handle.setLevel(file_level)

        simple_formatter = logging.Formatter(simple_formatter_confing)
        verbose_formatter = logging.Formatter(verbose_formatter_config)

        console_handle.setFormatter(simple_formatter)
        file_handle.setFormatter(verbose_formatter)

        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        return self.case_logger


do_logger = HandleLog().get_logger()

if __name__ == '__main__':
    case_logger = HandleLog().get_logger()
    case_logger.debug('这个是一个debug级别的日志信息')
    case_logger.info('这个是一个info级别的日志信息')
    case_logger.warning('这个是一个warning级别的日志信息')
    case_logger.error('这个是一个error级别的日志信息')
    case_logger.critical('这个是一个critical级别的日志信息')
