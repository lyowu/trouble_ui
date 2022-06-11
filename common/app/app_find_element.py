# -*- encoding=utf8 -*-
__author__ = "HB"
#移动端-元素查找
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


class AppFindElement:
    '''
    :param elementName: 元素名称
    :return element: 元素对象
    '''
    #通过name属性查找元素
    @staticmethod
    def find_element_by_name(elementName):
        try:
            return poco(elementName)
        except TargetNotFoundError as e:
            print("error_info:",e)

    '''
    :param elementText: 元素文本
    :return element: 元素对象
    '''
    #通过text属性查找元素
    @staticmethod
    def find_element_by_text(elementText):
        try:
            return poco(text=elementText)
        except TargetNotFoundError as e:
            print("error_info:",e)

    #通过rescource-id属性来查找元素
    @staticmethod
    def find_element_by_sid(elementSID):
        try:
            return poco(elementSID)
        except TargetNotFoundError as e:
            print("error_info:",e)