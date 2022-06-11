# -*- encoding=utf8 -*-

__author__ = "WLX"
#android端-搜索页
from page_class.android_element.app_world.common_app_package_page_element import PackagePageElement
from page_class.android_action.common_page_action import CommonPageAction
from common.app.app_wait import *
from common.app.app_assert_lib import *
from airtest.core.api import *
from img.android_ui_img.app_world_page_img.world_page_img_manage import ManageWorldPageImg
from airtest.core.cv import Template

# 子包页
class PubIntoPackagePage(AppAssert):

    # 进入子包入口：最近玩，默认子包
    def into_app_package_page(self):

        # 最近玩：点击 默认子包
        try:
            recent_play_index = PackagePageElement.recent_play_index()
            CommonPageAction.click(recent_play_index)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(10)

        # 子包内返回按钮
        touch(Template(ManageWorldPageImg.package_return_icon.value))



