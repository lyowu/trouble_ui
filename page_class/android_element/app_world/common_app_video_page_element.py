# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端--视频页--元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 视频页元素管理
class VideoPageElement:

    # 视频：暂停/播放按钮
    @staticmethod
    def video_pause_icon():
        video_pause_icon = "com.sinyee.babybus.world:id/iv_play"
        return AppFindElement.find_element_by_name(video_pause_icon)


    # 视频：全屏按钮
    @staticmethod
    def video_fullscreen_icon():
        video_fullscreen_icon = "com.sinyee.babybus.world:id/exo_content_frame"
        return AppFindElement.find_element_by_name(video_fullscreen_icon)

    # 视频：视频列表切换到第2个
    @staticmethod
    def video_list_switch():
        appFindElement = AppFindElement()
        video_list_switch = "com.sinyee.babybus.world:id/rv_video_list"
        video_list_item = appFindElement.find_element_by_name(video_list_switch)
        video_name = "android.widget.RelativeLayout"
        return video_list_item.child(video_name)[1]

    # 视频：视频返回按钮
    @staticmethod
    def video_back_button():
        video_back_button = "com.sinyee.babybus.world:id/iv_back"
        return AppFindElement.find_element_by_name(video_back_button)

    '''

    #痛過 airtesst圖片識別
    driver.airtest_touch(Template(CreateProjectReleasePageImg.panel_button.value))
    WebWait.wait(3)
    
    # 首页--推荐按钮
    @staticmethod
    def kids_recommend_icon():
        kids_recommend_icon = "推荐"
        return AppFindElement.find_element_by_text(kids_recommend_icon)

    # 首页--最近按钮
    @staticmethod
    def kids_latest_icon():
        kids_latest_icon = "最近"
        return AppFindElement.find_element_by_text(kids_latest_icon)

    @staticmethod
    def weibo_favorite_icon():
        weibo_favorite_icon = "收藏"
        return AppFindElement.find_element_by_text(weibo_favorite_icon)
    try:
        form_panel_button = HomePageElement.form_panel_button(driver)
        if form_panel_button != None:
            is_form_panel_button_exists = True
            CommonProjectFormAction.click(form_panel_button)
            WebWait.wait(3)
        else:
            is_form_panel_button_exists = False
            print("还未进入主页")
        self.assert_equal(is_form_panel_button_exists, True, "验证卡片入口是否存在")
    except AssertionError as e:
        print("error_info", e)
    
    '''