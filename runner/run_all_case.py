#-*-coding:utf-8 -*-
import unittest

from common.htmltestrunner.create_test_report import TestReport
from common.htmltestrunner.HTMLTestReportCN import HTMLTestRunner

# 测试用例存放路径
case_path = r'..\test_case'

# 获取所有测试用例
def get_all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_suit3*.py",top_level_dir=None)
    #discover = unittest.defaultTestLoader.discover(case_path, pattern="test_app_gp_world.py", top_level_dir=None)
    return discover

if __name__ == '__main__':
    #创建测试报告
    fq=TestReport.create_report()
    # 运行测试用例
    #runner = unittest.TextTestRunner(get_all_case)
    runner = HTMLTestRunner(stream=fq, title="测试报告", description="description")
    runner.run(get_all_case())

