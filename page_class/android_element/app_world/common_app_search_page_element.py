# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端-搜索页--元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 搜索页元素管理
class SearchPageElement:


    # 搜索页-输入框
    @staticmethod
    def world_search_input():
        world_search_input = "com.sinyee.babybus.world:id/etSearch"
        return AppFindElement.find_element_by_name(world_search_input)

    # 搜索页-搜索按钮
    @staticmethod
    def world_search_button():
        world_search_button = "com.sinyee.babybus.world:id/llSearch"
        return AppFindElement.find_element_by_name(world_search_button)

    # 搜索页-子包搜索结果
    @staticmethod
    def app_search_result():
        app_text = poco('com.sinyee.babybus.world:id/bottom_layout').child('com.sinyee.babybus.world:id/world_title').get_text()
        return app_text

    # 搜索页-视频搜索结果
    @staticmethod
    def video_search_result():
        video_text = poco('com.sinyee.babybus.world:id/bottom_layout').child('com.sinyee.babybus.world:id/album_title').get_text()
        return video_text

    ####
    @staticmethod
    def world_search_list():
        #menuList1 = poco("com.sinyee.babybus.world:id/rv").child("android.widget.RelativeLayout")
        menuList1 = poco("com.sinyee.babybus.world:id/root").child("com.sinyee.babybus.world:id/rv")
        for i in range(0,len(list(menuList1))):
            return menuList1[i]

    # 搜索页-暂无内容
    @staticmethod
    def world_search_empty():
        world_search_empty = "com.sinyee.babybus.world:id/empty"
        return AppFindElement.find_element_by_name(world_search_empty)

    # 搜索结果页-切换到 视频 标签
    @staticmethod
    def switch_video_button():
        switch_video_button = "com.sinyee.babybus.world:id/tvVideo"
        return AppFindElement.find_element_by_name(switch_video_button)

    # 视频标签：第一个视频图标
    @staticmethod
    def video_search_index():
        appFindElement = AppFindElement()
        video_search_index = "com.sinyee.babybus.world:id/rv"
        video_search_result = appFindElement.find_element_by_name(video_search_index)
        videosearch_name = "android.widget.RelativeLayout"
        return video_search_result.child(videosearch_name)[0]

    # 搜索页-返回按钮
    @staticmethod
    def search_back_button():
        search_back_button = "com.sinyee.babybus.world:id/llBack"
        return AppFindElement.find_element_by_name(search_back_button)

    # 热搜：第一个 热搜词
    @staticmethod
    def hot_search_index():
        appFindElement = AppFindElement()
        hot_search_index = "com.sinyee.babybus.world:id/lv"
        hot_search_security = appFindElement.find_element_by_name(hot_search_index)
        hotsearch_name = "android.widget.LinearLayout"
        return hot_search_security.child(hotsearch_name)[0]

    # 搜索页-热搜词
    @staticmethod
    def hot_search_word():
        hot_word = poco('com.sinyee.babybus.world:id/lv').child('android.widget.LinearLayout').child('com.sinyee.babybus.world:id/tvName').get_text()
        return hot_word

    # 搜索页 右侧默认第一个子包
    @staticmethod
    def default_app_index():
        appFindElement = AppFindElement()
        default_app_index = "com.sinyee.babybus.world:id/rv"
        default_app_item = appFindElement.find_element_by_name(default_app_index)
        default_name = "android.widget.RelativeLayout"
        return default_app_item.child(default_name)[0]

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