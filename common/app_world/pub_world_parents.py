# -*- encoding=utf8 -*-

__author__ = "WLX"
#android端-家长中心页
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from page_class.android_element.app_world.common_app_home_page_element import HomePageElement
from page_class.android_element.app_world.common_app_search_page_element import SearchPageElement
from page_class.android_action.common_page_action import CommonPageAction
from common.app.app_wait import *
from common.app.app_assert_lib import *
from test_data.base_data import PandaWorld
from img.android_ui_img.app_kids_page_img.kids_google_page_img_manage import ManageKidsGooglePageImg
from airtest.core.cv import Template

# 首页
class PubIntoSearchPage(AppAssert):

    # 搜索功能：普通搜索的能力
    def into_app_search_page(self):

        # 首页顶部菜单栏--搜索入口
        try:
            world_menu_search = HomePageElement.world_menu_search()
            if world_menu_search != None:
                is_world_menu_search_exists = True
            else:
                is_world_menu_search_exists = False
            self.assert_equal(is_world_menu_search_exists, True, "验证搜索入口是否存在")
            CommonPageAction.click(world_menu_search)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

        # 输入关键字 + 搜索
        try:
            world_search_input = SearchPageElement.world_search_input()
            CommonPageAction.input(world_search_input, PandaWorld.searchContent.value)
            AppWait.wait(3)
            #CommonPageAction.keyboard_click("KEYCODE_ENTER")
            world_search_button = SearchPageElement.world_search_button()
            CommonPageAction.click(world_search_button)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 搜索结果页--切换至 视频 标签
        try:
            switch_video_button = SearchPageElement.switch_video_button()
            if switch_video_button != None:
                is_switch_video_button_exists = True
            else:
                is_switch_video_button_exists = False
            self.assert_equal(is_switch_video_button_exists, True, "验证视频标签是否存在")
            CommonPageAction.click(switch_video_button)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

        # 搜索结果页--视频 标签--点击第一个视频
        try:
            video_search_index = SearchPageElement.video_search_index()
            if video_search_index != None:
                is_video_search_index_exists = True
            else:
                is_video_search_index_exists = False
            self.assert_equal(is_video_search_index_exists, True, "验证视频是否存在")
            CommonPageAction.click(video_search_index)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(1)



    # 搜索功能：热搜能力
    def app_hotsearch_page(self):

        # 首页顶部菜单栏--搜索入口
        try:
            world_menu_search = HomePageElement.world_menu_search()
            if world_menu_search != None:
                is_world_menu_search_exists = True
            else:
                is_world_menu_search_exists = False
            self.assert_equal(is_world_menu_search_exists, True, "验证搜索入口是否存在")
            CommonPageAction.click(world_menu_search)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

        # 搜索页点击 热搜区 第一个 【安全】
        try:
            hot_search_index = SearchPageElement.hot_search_index()
            CommonPageAction.click(hot_search_index)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 搜索页 返回 主页
        try:
            search_back_button = SearchPageElement.search_back_button()
            CommonPageAction.click(search_back_button)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
