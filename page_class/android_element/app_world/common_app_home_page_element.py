# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端-熊猫世界主页--元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 首页元素管理
class HomePageElement:

    # 顶部tab栏
    @staticmethod
    def world_tab_index():
        appFindElement = AppFindElement()
        world_tab_index = "com.sinyee.babybus.world:id/tab_index_recyclerview"
        world_tab_num = appFindElement.find_element_by_name(world_tab_index)
        access_name = "android.widget.RelativeLayout"
        return world_tab_num.child(access_name)[0]

    # 首页顶部菜单栏--搜索入口
    @staticmethod
    def world_menu_search():
        world_menu_search = "com.sinyee.babybus.world:id/iv_search_icon"
        return AppFindElement.find_element_by_name(world_menu_search)



    '''
    
    # tab [推荐]按钮
    @staticmethod
    def kids_recommend_icon():
        appFindElement = AppFindElement()
        world1232_menu_setting = "com.sinyee.babybus.world:id/img_menu_setting"
        kids_recommend_icon = appFindElement.find_element_by_name(world1232_menu_setting)
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


    # 【推荐】对应的 箭头位置
    @staticmethod
    def kids_recently_list():
        appFindElement = AppFindElement()
        kids_resource_panel = "com.sinyee.babybus.kids:id/classify_content_item"
        kids_resource_list = appFindElement.find_element_by_name(kids_resource_panel)
        first_resource = "android.widget.RelativeLayout"
        return kids_resource_list.child(first_resource)[0]


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