# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端-gp世界主页--元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 首页元素管理
class HomePageElement:

    # 新品弹窗 关闭按钮
    @staticmethod
    def new_pop_close():
        new_pop_close = "com.sinyee.babybus.world:id/close2"
        return AppFindElement.find_element_by_name(new_pop_close)

    # 设置 入口元素
    @staticmethod
    def world_menu_setting():
        world_menu_setting = "com.sinyee.babybus.world:id/img_menu_setting"
        return AppFindElement.find_element_by_name(world_menu_setting)

    # 顶部tab栏
    @staticmethod
    def world_tab_index():
        appFindElement = AppFindElement()
        world_tab_index = "com.sinyee.babybus.world:id/tab_index_recyclerview"
        world_tab_num = appFindElement.find_element_by_name(world_tab_index)
        access_name = "android.widget.RelativeLayout"
        return world_tab_num.child(access_name)[1]

    # 顶部tab栏
    @staticmethod
    def home_page_index():
        tab_index = poco("com.sinyee.babybus.world:id/tab_recyclerview").children()
        return tab_index

    # tab对应的[主页]标签控件
    @staticmethod
    def world_main_index():
        main_index = poco("com.sinyee.babybus.world:id/main_recyclerview").children()
        main_sub_index = main_index[1].child('com.sinyee.babybus.world:id/classify_content_layout').child('com.sinyee.babybus.world:id/tagView_layout')
        return main_sub_index

    # 默认子包
    @staticmethod
    def default_app_index():
        app_index = poco("com.sinyee.babybus.world:id/main_recyclerview").children()
        app_sub_index = app_index[0].child('com.sinyee.babybus.world:id/classify_content_layout')
        default_child = app_sub_index.child('com.sinyee.babybus.world:id/classify_content_item')
        default_app = default_child.child('android.widget.RelativeLayout')
        return default_app

    # 最后一个tab 的第一个子包/video
    @staticmethod
    def specific_app_index(index_num):
        app_index = poco("com.sinyee.babybus.world:id/main_recyclerview").children()
        app_sub_index = app_index[index_num]
        specific_child = app_sub_index.child('com.sinyee.babybus.world:id/classify_content_layout').child('com.sinyee.babybus.world:id/classify_content_item')
        specific_app = specific_child.children()
        return specific_app[0]

    # 课程
    @staticmethod
    def course_page_index():
        course_index = poco("com.sinyee.babybus.world:id/main_recyclerview").children()
        course_page_index = course_index[0]
        return course_page_index

