# -*- coding: utf-8 -*-
from bin.HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os
import yagmail

''' 
1、初始化：python -m uiautomator2 init
2、元素抓取：python -m weditor
'''


def collect_use_cases():
    cur_path = os.path.abspath('..') + '/test_case/'
    discover = unittest.defaultTestLoader.discover(cur_path, pattern="case*.py", top_level_dir=None)
    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    report_dir = os.path.abspath('..') + '/output/test_report/'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    report_path = report_dir + now + "-result.html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告：', description=u'用例执行情况：')
    runner.run(discover)
    fp.close()
    return report_path


def send_report_email(report_path):
    yag = yagmail.SMTP(user="xxx", password="xxx", host="smtp.126.com")
    contents = ['邮件正文', '用例执行情况：']
    addressee = ['xx@qq.com', 'xxx@qq.com']
    yag.send(addressee, '邮件主题', contents, report_path)


if __name__ == '__main__':
    collect_use_cases()
    # send_report_email(collect_use_cases())
