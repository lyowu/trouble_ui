# -*- encoding=utf8 -*-

__author__ = "WLX"
#android端-首页
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from page_class.android_element.app_world_google.common_app_home_page_element import HomePageElement
from page_class.android_action.app_world_google.common_page_action import CommonPageAction
from common.app.app_wait import *
from common.app.app_assert_lib import *
from img.android_ui_img.app_gp_world_page_img.world_page_img_manage import ManageGpWorldPageImg
from airtest.core.cv import Template
from page_class.android_element.app_world_google.common_app_course_page_element import CoursePageElement

class PubIntoHomePage(AppAssert):

    # 首页顶部tab切换
    def home_page_tab_switch(self):

        # 第3步：首页 切换tab
        home_page_index = HomePageElement.home_page_index()
        AppWait.wait(1)
        # 点每个tab，再去看 主页的tab_name是否存在
        try:
            for i in range(1, len(list(home_page_index))):
                CommonPageAction.click(home_page_index[i])
                # 验证切tab，主页数据校验
                world_main_index = HomePageElement.world_main_index()
                if world_main_index != None:
                    is_world_main_index_exists = True
                else:
                    is_world_main_index_exists = False
                self.assert_equal(is_world_main_index_exists, True, "验证主页tab是否存在")
                AppWait.wait(1)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(1)

    # 新品弹窗，关闭
    def new_pop_window(self):

        try:
            # 第1步：先关掉新品弹窗
            new_pop_close = HomePageElement.new_pop_close()
            if new_pop_close != None:
                is_new_pop_close_exists = True
            else:
                is_new_pop_close_exists = False
            self.assert_equal(is_new_pop_close_exists, True, "验证新品弹窗的关闭是否存在")
            CommonPageAction.click(new_pop_close)
            AppWait.wait(1)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(1)

    # 进入默认子包
    def into_default_app_fun(self):

        try:
            # 第2步：进入默认子包 美食
            default_app_index = HomePageElement.default_app_index()
            if default_app_index != None:
                is_default_app_index_exists = True
            else:
                is_default_app_index_exists = False
            self.assert_equal(is_default_app_index_exists, True, "验证默认子包是否存在")
            CommonPageAction.click(default_app_index)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        touch(Template(r"E:\UI_Automation\UITestForBabybus_New\img\android_ui_img\app_gp_world_page_img\game_back.png"))
        AppWait.wait(1)

    # 进入特定的 子包
    def into_specific_app_fun(self):
        try:
            #
            # 首页切到对应tab
            home_page_index = HomePageElement.home_page_index()
            CommonPageAction.click(home_page_index[2])
            AppWait.wait(1)
            # 第一个tab 的视频
            specific_app_index = HomePageElement.specific_app_index(2)
            if specific_app_index != None:
                is_specific_app_index_exists = True
            else:
                is_specific_app_index_exists = False
            self.assert_equal(is_specific_app_index_exists, True, "验证要下载的子包是否存在")
            CommonPageAction.click(specific_app_index)
            AppWait.wait(12)
        except AssertionError as e:
            print("error_info", e)
        touch(Template(
            r"E:\UI_Automation\UITestForBabybus_New\img\android_ui_img\app_gp_world_page_img\game_back.png"))
        AppWait.wait(1)


    # 进入特定的video
    def into_specific_video_fun(self):
        try:
            # 首页切到对应tab
            home_page_index = HomePageElement.home_page_index()
            CommonPageAction.click(home_page_index[2])
            AppWait.wait(1)
            # 第一个tab 的视频
            specific_app_index = HomePageElement.specific_app_index(0)
            if specific_app_index != None:
                is_specific_app_index_exists = True
            else:
                is_specific_app_index_exists = False
            self.assert_equal(is_specific_app_index_exists, True, "验证要下载的视频是否存在")
            CommonPageAction.click(specific_app_index)
            AppWait.wait(10)
        except AssertionError as e:
            print("error_info", e)
        keyevent("BACK")
        AppWait.wait(1)
        #keyevent("BACK")


    # 进入课程
    def into_course_fun(self):

        try:
            # 首页切到对应tab
            home_page_index = HomePageElement.home_page_index()
            CommonPageAction.click(home_page_index[4])
            AppWait.wait(1)
            # 点击首页的课程入口
            course_page_index = HomePageElement.course_page_index()
            CommonPageAction.click(course_page_index)
            AppWait.wait(2)
            # 断言是否进入课程
            course_tab_icon = CoursePageElement.course_tab_icon()
            if course_tab_icon != None:
                is_course_tab_icon_exists = True
            else:
                is_course_tab_icon_exists = False
            self.assert_equal(is_course_tab_icon_exists, True, "验证是否进入课程页")
            AppWait.wait(2)
            # 选择第一个，进入课程
            course_list_index = CoursePageElement.course_list_index(0)
            CommonPageAction.click(course_list_index)
            AppWait.wait(12)

            touch(Template(
                r"E:\UI_Automation\UITestForBabybus_Translate\img\android_ui_img\app_gp_world_page_img\course_game_back.png"))
            # 返回首页
            course_back_button = CoursePageElement.course_back_button()
            CommonPageAction.click(course_back_button)
            AppWait.wait(1)
        except AssertionError as e:
            print("error_info", e)

        AppWait.wait(1)



# 进入家长中心
class PubIntoParentCenterPage(AppAssert):

    # 首页进入家长中心入口
    def into_parent_center_page(self):

        # 设置按钮进入家长中心 （自动化测试包，自动过滤验证环节）
        try:
            world_setting_access = HomePageElement.world_menu_setting()
            if world_setting_access != None:
                is_world_setting_access_exists = True
            else:
                is_world_setting_access_exists = False
            self.assert_equal(is_world_setting_access_exists, True, "验证家长中心是否存在")
            CommonPageAction.click(world_setting_access)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

