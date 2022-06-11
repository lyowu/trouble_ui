# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端-学习页面-元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#学习页面元素
class LearnPageElement:
    #搜索按钮
    @staticmethod
    def search_button():
        appFindElement=AppFindElement()
        search_button_name="com.nd.app.factory.ap1537932799363:id/action_search"
        return appFindElement.find_element_by_name(search_button_name)