# -*- encoding=utf8 -*-

__author__ = "WLX"
#android端-视频页

from page_class.android_element.app_world.common_app_video_page_element import VideoPageElement
from page_class.android_action.common_page_action import CommonPageAction
from common.app.app_wait import *
from common.app.app_assert_lib import *
from airtest.core.api import *
from img.android_ui_img.app_world_page_img.world_page_img_manage import ManageWorldPageImg
from airtest.core.cv import Template


# 视频页
class PubIntoVideoPage(AppAssert):

    # 进入子包入口：最近玩，默认子包
    def into_app_video_page(self):

        # 视频：全屏 切 默认屏
        try:
            video_fullscreen_icon = VideoPageElement.video_fullscreen_icon()
            CommonPageAction.click(video_fullscreen_icon)
            AppWait.wait(1)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(0)

        '''
       try:

            video_pause_icon = VideoPageElement.video_pause_icon()
            CommonPageAction.click(video_pause_icon)
            AppWait.wait(1)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(1)

        # video 点暂停按钮
        #touch(Template(ManageWorldPageImg.video_pause_icon.value))
        

        # 视频：视频列表切换到第2个
        try:
            video_list_switch = VideoPageElement.video_list_switch()
            CommonPageAction.click(video_list_switch)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(5)

        # 视频：全屏 切 默认屏
        try:
            video_fullscreen_icon = VideoPageElement.video_fullscreen_icon()
            CommonPageAction.click(video_fullscreen_icon)
            AppWait.wait(1)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(1)
        
        # 视频：视频返回按钮
        try:
            video_back_button = VideoPageElement.video_back_button()
            CommonPageAction.click(video_back_button)
            AppWait.wait(2)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(2)
        '''
        #touch(Template(ManageWorldPageImg.video_back_icon.value))
        keyevent("BACK")
