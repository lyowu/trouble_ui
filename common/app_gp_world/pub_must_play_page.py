# -*- encoding=utf8 -*-

__author__ = "WLX"
#android端- 必玩页
import re

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from page_class.android_element.app_world_google.common_app_must_play_element import MustPlayPageElement
from page_class.android_action.app_world_google.common_page_action import CommonPageAction
from common.app.app_wait import *
from common.app.app_assert_lib import *
from img.android_ui_img.app_gp_world_page_img.world_page_img_manage import ManageGpWorldPageImg
from airtest.core.cv import Template
from common.app_gp_world.pub_excel_data_value import PubExcelOperator

# 必玩页
class PubIntoMustPlayPage(AppAssert):

    def must_play_translation(self,excel_Column):

        try:
            # 参数：对应列的值，1是第2列，可以指定对应的列
            # zh-CN: 1  en: 2
            excel_list = PubExcelOperator.get_excel_last2colum(excel_Column)
            AppWait.wait(2)
            element_list = []
            # 弹窗-主标题
            title_text_result = MustPlayPageElement.title_text_result()
            element_list.append(title_text_result)
            # 弹窗-副标题
            subtitle_text_result = MustPlayPageElement.subtitle_text_result()
            element_list.append(subtitle_text_result)

            # 弹窗--按钮文案
            must_download_text = MustPlayPageElement.must_download_text()
            element_list.append(must_download_text)
            #print(excel_list)
            #print(element_list)

            if element_list == excel_list:
                is_must_play_text_exists = True
            else:
                is_must_play_text_exists = False

                # 对比2个List的区别
                defferent_list = set(element_list).difference(set(excel_list))
                print('跟文档不一致的选项：', defferent_list)
            self.assert_equal(is_must_play_text_exists, True, "验证翻译是否正确")

        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

    # 必玩页 业务逻辑（新）
    def must_play_popup(self):
        try:
            # 验证必玩弹窗、标题是否存在
            must_play_popup = MustPlayPageElement.must_play_popup()

            must_download_button = MustPlayPageElement.must_download_button()

            if must_play_popup != None and must_download_button != None:
                is_must_play_popup_exists = True
            else:
                is_must_play_popup_exists = False
            self.assert_equal(is_must_play_popup_exists, True, "验证必玩弹窗是否存在")
            CommonPageAction.click(must_download_button)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)


