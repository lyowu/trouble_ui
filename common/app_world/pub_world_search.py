# -*- encoding=utf8 -*-

__author__ = "WLX"
#android端-搜索页
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from page_class.android_element.app_world.common_app_search_page_element import SearchPageElement
from page_class.android_action.common_page_action import CommonPageAction
from common.app.app_wait import *
from common.app.app_assert_lib import *
from test_data.base_data import PandaWorld
from img.android_ui_img.app_world_page_img.world_page_img_manage import ManageWorldPageImg
from airtest.core.cv import Template


# 搜索类，管理搜索相关的能力
class PubIntoSearchPage(AppAssert):

    # 1、热搜
    def app_hotsearch_page(self):

        # 搜索页点击 热搜区 第一个 【元宵】
        global hot_word
        try:
            #获取左侧第一个热搜词的text
            hot_word = SearchPageElement.hot_search_word()
            #点击左侧第一个热搜词
            hot_search_index = SearchPageElement.hot_search_index()
            CommonPageAction.click(hot_search_index)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 搜索结果校验
        try:
            app_search_result = SearchPageElement.app_search_result()
            if hot_word in app_search_result:
                is_world_search_result_exists = True
            else:
                is_world_search_result_exists = False
            self.assert_equal(is_world_search_result_exists, True, "验证搜索结果是否正确")

        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)

    # 2、常规词搜索
    def into_app_search_page(self):

        # 输入关键字 + 搜索
        try:
            world_search_input = SearchPageElement.world_search_input()
            if world_search_input != None:
                is_world_search_input_exists = True
            else:
                is_world_search_input_exists = False
            self.assert_equal(is_world_search_input_exists, True, "验证搜索输入框是否存在")
            CommonPageAction.input(world_search_input, PandaWorld.searchContent.value)
            AppWait.wait(3)
            #CommonPageAction.keyboard_click("KEYCODE_ENTER")
            world_search_button = SearchPageElement.world_search_button()
            CommonPageAction.click(world_search_button)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 搜索结果校验
        try:
            app_search_result = SearchPageElement.app_search_result()
            if PandaWorld.searchContent.value in app_search_result:
                is_world_search_result_exists = True
            else:
                is_world_search_result_exists = False
            self.assert_equal(is_world_search_result_exists, True, "验证搜索结果是否正确")

        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)

        # 搜索结果页--切换至 视频 标签
        try:
            switch_video_button = SearchPageElement.switch_video_button()
            if switch_video_button != None:
                is_switch_video_button_exists = True
            else:
                is_switch_video_button_exists = False
            self.assert_equal(is_switch_video_button_exists, True, "验证搜索结果是否存在应用和视频入口")
            CommonPageAction.click(switch_video_button)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

        # 搜索结果校验--视频 标签--第一个视频
        try:
            video_search_result = SearchPageElement.video_search_result()
            if PandaWorld.searchContent.value in video_search_result:
                is_world_search_result_exists = True
            else:
                is_world_search_result_exists = False
            self.assert_equal(is_world_search_result_exists, True, "验证搜索结果是否正确")
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(1)

    # 3、无效词搜索
    def into_app_empty_page(self):

        # 输入关键字 + 搜索
        try:
            world_search_input = SearchPageElement.world_search_input()
            CommonPageAction.input(world_search_input, PandaWorld.invalidContent.value)
            AppWait.wait(3)
            world_search_button = SearchPageElement.world_search_button()
            CommonPageAction.click(world_search_button)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 搜索结果页--通过是否【暂无内容】判断搜索结果
        try:
            world_search_empty = SearchPageElement.world_search_empty()
            if world_search_empty != None:
                is_world_search_empty_exists = True
            else:
                is_world_search_empty_exists = False
            self.assert_equal(is_world_search_empty_exists, True, "验证搜索结果是否存在")
        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)

    # 4、搜索页进入子包
    def search_into_app_page(self):

        # 点击 搜索页 默认第一个子包
        try:
            default_app_index = SearchPageElement.default_app_index()
            AppWait.wait(3)
            CommonPageAction.click(default_app_index)
            AppWait.wait(8)
        except AssertionError as e:
            print("error_info", e)

        # 断言 子包主页 左上角 返回按钮
        try:
            back_icon = Template(ManageWorldPageImg.app_back_icon.value)
            if back_icon != None:
                is_back_icon_exists = True
            else:
                is_back_icon_exists = False
            self.assert_equal(is_back_icon_exists, True, "验证搜索结果是否存在")
        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)

        # 物理 返回 搜索页
        CommonPageAction.keyboard_click("BACK")
        #keyevent("BACK")
            
        

