# -*- encoding=utf8 -*-
__author__ = "WLX"
#创建报告
import sys
import os
import datetime
sys.path.append(r'..\commom\htmltestrunner')

class TestReport:
    #创建报告文件夹
    @staticmethod
    def create_report():
        #申明文件路径
        test_report_path = r'E:\UI_Automation\UITestForBabybus_New\test_report'  # 报告根路径
        now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")  # 报告命名时间格式化
        report_path = test_report_path + "\\" + now  # 报告文件路径
        #创建文件夹
        def create_report_dir(dir):
            try:
                if not os.path.exists(dir):
                    os.makedirs(dir)
                else:
                    print("文件路径已存在")
            except:
                print("创建报告文件夹失败")
        #创建报告根目录
        create_report_dir(test_report_path)
        create_report_dir(report_path)
        #定义并创建报告文件
        report_file = datetime.datetime.now().strftime("%Y%m%dT%H%M%S") + "_res.html"
        fq = open(os.path.join(report_path,report_file),"wb")
        return fq








