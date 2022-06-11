# -*- encoding=utf8 -*-
__author__ = "HB"
#android端-搜索结果页面-元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

class SearchResultPageElement():
    #搜索结果对象
    @staticmethod
    def search_result():
        appFindElement = AppFindElement()
        search_result_list_name = "com.nd.app.factory.ap1537932799363:id/rv_search_list"
        search_result_list = appFindElement.find_element_by_name(search_result_list_name)
        job_name = "com.nd.app.factory.ap1537932799363:id/rl_job_job"
        return search_result_list.child(job_name)[0]
