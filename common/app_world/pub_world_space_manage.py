# -*- encoding=utf8 -*-

__author__ = "WLX"
#android端-空间管理页
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

from page_class.android_element.app_world.common_app_space_page_element import SpaceManagePageElement
from page_class.android_action.common_page_action import CommonPageAction
from common.app.app_wait import *
from common.app.app_assert_lib import *
from test_data.base_data import PandaWorld
from img.android_ui_img.app_world_page_img.world_page_img_manage import ManageWorldPageImg
from airtest.core.cv import Template


# 空间管理
class PubMangeSpacePage(AppAssert):

    # 1、已下载子包清理
    def download_app_page(self):

        try:
            #点击 已下载中复选框
            app_check_box = SpaceManagePageElement.app_check_box()
            if app_check_box != None:
                is_app_check_box_exists = True
            else:
                is_app_check_box_exists = False
            self.assert_equal(is_app_check_box_exists, True, "验证子包选中框是否存在")
            CommonPageAction.click(app_check_box)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 点击 删除按钮
        try:
            app_delete_button = SpaceManagePageElement.app_delete_button()
            if app_delete_button != None:
                is_app_delete_button_exists = True
            else:
                is_app_delete_button_exists = False
            self.assert_equal(is_app_delete_button_exists, True, "验证删除按钮是否存在")
            CommonPageAction.click(app_delete_button)
        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)

        # 二次确认框 ，点击确认
        try:
            delete_confirm_button = SpaceManagePageElement.delete_confirm_button()
            if delete_confirm_button != None:
                is_delete_confirm_button_exists = True
            else:
                is_delete_confirm_button_exists = False
            self.assert_equal(is_delete_confirm_button_exists, True, "验证二次确认框确认按钮是否存在")
            CommonPageAction.click(delete_confirm_button)
        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)

        # 验证删除结果
        try:
            no_data_tip = SpaceManagePageElement.no_data_tip()
            if no_data_tip != None:
                is_no_data_tip_exists = True
            else:
                is_no_data_tip_exists = False
            self.assert_equal(is_no_data_tip_exists, True, "验证是否删除")
        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)

    # 2、视频缓存清理
    def download_video_page(self):

        # 输入关键字 + 搜索
        try:
            world_search_input = FeedbackPageElement.world_search_input()
            if world_search_input != None:
                is_world_search_input_exists = True
            else:
                is_world_search_input_exists = False
            self.assert_equal(is_world_search_input_exists, True, "验证搜索输入框是否存在")
            CommonPageAction.input(world_search_input, PandaWorld.searchFeedback.value)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 搜索结果校验
        try:
            word_search_title = FeedbackPageElement.word_search_title()
            word_search_context = FeedbackPageElement.word_search_context()
            if PandaWorld.searchFeedback.value in word_search_title and PandaWorld.searchFeedback.value in word_search_context :
                is_word_search_result_exists = True
            else:
                is_word_search_result_exists = False
            self.assert_equal(is_word_search_result_exists, True, "验证搜索结果是否正确")

        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)


