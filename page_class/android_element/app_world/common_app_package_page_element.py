# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端-子包页--元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 子包页元素管理
class PackagePageElement:

    # 最近玩：默认子包 入口
    @staticmethod
    def recent_play_index():
        appFindElement = AppFindElement()
        recent_play_index = "com.sinyee.babybus.world:id/classify_content_item"
        recent_play_item = appFindElement.find_element_by_name(recent_play_index)
        default_app = "android.widget.RelativeLayout"
        return recent_play_item.child(default_app)[0]

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