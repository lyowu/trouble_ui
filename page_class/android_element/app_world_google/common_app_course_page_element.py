# -*- encoding=utf8 -*-
__author__ = "WLX"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 课程页元素
class CoursePageElement:

    # 课程页返回按钮，一级页
    @staticmethod
    def course_back_button():
        course_back_button = "com.sinyee.babybus.world:id/iv_back"
        return AppFindElement.find_element_by_name(course_back_button)

    # 课程页顶部tab
    @staticmethod
    def course_tab_icon():
        course_tab_icon = "com.sinyee.babybus.world:id/iv_course_tab"
        return AppFindElement.find_element_by_name(course_tab_icon)

    # 课程列表索引
    @staticmethod
    def course_list_index(index_num):
        app_index = poco("com.sinyee.babybus.world:id/rv_course").children()
        return app_index[index_num]

