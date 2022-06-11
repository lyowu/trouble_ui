# -*- encoding=utf8 -*-
__author__ = "HB"
#android端-搜索页面-元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
class SearchPageElement:
    #输入框
    @staticmethod
    def search_input():
        search_input_name = "com.nd.app.factory.ap1537932799363:id/search_src_text"
        return AppFindElement.find_element_by_name(search_input_name)

