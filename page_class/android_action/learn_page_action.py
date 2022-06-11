# -*- encoding=utf8 -*-
__author__ = "HB"
#android端-学习页面-操作
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#学习页面操作
class LearnPageAction:
    #点击操作
    @staticmethod
    def click(element):
        element.click()