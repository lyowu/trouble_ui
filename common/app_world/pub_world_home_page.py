# -*- encoding=utf8 -*-

__author__ = "WLX"
#android端-首页
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from page_class.android_element.app_world.common_app_home_page_element import HomePageElement
from page_class.android_action.common_page_action import CommonPageAction
from common.app.app_wait import *
from common.app.app_assert_lib import *
from test_data.base_data import PandaWorld
from img.android_ui_img.app_kids_page_img.kids_google_page_img_manage import ManageKidsGooglePageImg
from airtest.core.cv import Template

# 首页
class PubIntoHomePage(AppAssert):

    # 首页顶部tab功能
    def into_app_home_page(self):

        # 首页 顶部tab
        try:
            world_tab_index = HomePageElement.world_tab_index()
            CommonPageAction.click(world_tab_index)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

    # 首页搜索入口
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


        '''
        # 点击 搜索结果
        try:
            weibo_search_result = WritePageElement.weibo_search_result()
            if weibo_search_result != None:
                is_weibo_search_result_exists = True
            else:
                is_weibo_search_result_exists = False
            self.assert_equal(is_weibo_search_result_exists, True, "验证搜索结果对不对")
            CommonPageAction.click(weibo_search_result)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        
        # 顶部tab栏 入口切换
        try:
            world_tab_index = HomePageElement.world_tab_index()
            CommonPageAction.click(world_tab_index)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

        # 太阳切月亮（开启夜间模式）入口
        try:
            world_switch_sun = HomePageElement.world_switch_sun()
            if world_switch_sun != None:
                is_world_switch_sun_exists = True
            else:
                is_world_switch_sun_exists = False
            self.assert_equal(is_world_switch_sun_exists, True, "验证太阳入口是否存在")
            CommonPageAction.click(world_switch_sun)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

        # 月亮切太阳（开启白天模式）入口
        try:
            world_switch_moon = HomePageElement.world_switch_moon()
            if world_switch_moon != None:
                is_world_switch_moon_exists = True
            else:
                is_world_switch_moon_exists = False
            self.assert_equal(is_world_switch_moon_exists, True, "验证月亮入口是否存在")
            CommonPageAction.click(world_switch_moon)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

        # vip入口进入订阅页面
        try:
            world_vip_access = HomePageElement.world_menu_vip()
            if world_vip_access != None:
                is_world_vip_access_exists = True
            else:
                is_world_vip_access_exists = False
            self.assert_equal(is_world_vip_access_exists, True, "验证vip订阅入口是否存在")
            CommonPageAction.click(world_vip_access)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

        # 订阅页面 关闭按钮 回到主页
        try:
            world_vip_close = HomePageElement.world_vip_close()
            if world_vip_close != None:
                is_world_vip_close_exists = True
            else:
                is_world_vip_close_exists = False
            self.assert_equal(is_world_vip_close_exists, True, "验证订阅页关闭按钮是否存在")
            CommonPageAction.click(world_vip_close)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)


        # 设置按钮进入家长中心 （自动化测试包，自动过滤验证环节）
        try:
            world_setting_access = HomePageElement.world_menu_setting()
            CommonPageAction.click(world_setting_access)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)
        '''


