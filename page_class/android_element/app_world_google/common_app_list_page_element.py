# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端-微博详情页--元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


class HomePageElement:

    # tab [推荐]按钮
    @staticmethod
    def kids_recommend_icon():
        appFindElement = AppFindElement()
        kids_tab_bannel = "com.sinyee.babybus.kids:id/tab_index_recyclerview"
        kids_recommend_icon = appFindElement.find_element_by_name(kids_tab_bannel)
        icon_name = "android.widget.RelativeLayout"
        return kids_recommend_icon.child(icon_name)[0]

    # 【推荐】对应的 箭头位置
    @staticmethod
    def kids_recommend_access():
        appFindElement = AppFindElement()
        kids_middle_bannel = "com.sinyee.babybus.kids:id/world_main_recyclerview"
        kids_middle_icon = appFindElement.find_element_by_name(kids_middle_bannel)
        access_name = "android.widget.RelativeLayout"
        return kids_middle_icon.child(access_name)[2]

    # 【推荐】列表页，左上角 【关闭】 按钮
    @staticmethod
    def recommend_close_icon():
        recommend_close_icon = "com.sinyee.babybus.kids:id/iv_close"
        return AppFindElement.find_element_by_name(recommend_close_icon)

    # 【推荐】列表页，右上角 【垃圾桶】 按钮
    @staticmethod
    def recommend_editor_icon():
        recommend_editor_icon = "com.sinyee.babybus.kids:id/iv_editor"
        return AppFindElement.find_element_by_name(recommend_editor_icon)

    # 【推荐】对应的 箭头位置
    @staticmethod
    def kids_recently_list():
        appFindElement = AppFindElement()
        kids_resource_panel = "com.sinyee.babybus.kids:id/classify_content_item"
        kids_resource_list = appFindElement.find_element_by_name(kids_resource_panel)
        first_resource = "android.widget.RelativeLayout"
        return kids_resource_list.child(first_resource)[0]

    # 【推荐】delete按钮
    @staticmethod
    def recommend_delete_icon():
        recommend_delete_icon = "com.sinyee.babybus.kids:id/iv_editor_delete"
        return AppFindElement.find_element_by_name(recommend_delete_icon)

    # 二次确认框--确认按钮
    @staticmethod
    def delete_confirm_button():
        delete_confirm_button = "com.sinyee.babybus.kids:id/confirm"
        return AppFindElement.find_element_by_name(delete_confirm_button)

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
    '''

    # 右上角设置按钮
    @staticmethod
    def kids_setting_icon():
        kids_setting_icon = "com.sinyee.babybus.kids:id/iv_setting"
        return AppFindElement.find_element_by_name(kids_setting_icon)

    '''
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