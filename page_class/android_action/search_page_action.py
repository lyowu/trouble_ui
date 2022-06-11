# -*- encoding=utf8 -*-
__author__ = "HB"
#android端-学习页面-操作
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

class SearchPageAction:
    @staticmethod
    #输入操作
    def input(element,key):
        element.set_text(key)

    @staticmethod
    #键盘点击
    def keyboard_click(key):
        keyevent(key)


