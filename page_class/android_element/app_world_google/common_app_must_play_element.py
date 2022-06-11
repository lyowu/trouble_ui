# -*- encoding=utf8 -*-
__author__ = "WLX"
#android-gp world must play page element
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 必玩页元素管理
class MustPlayPageElement:

    # 必玩弹窗
    @staticmethod
    def must_play_popup():
        must_play_popup = "com.sinyee.babybus.world:id/centerPopupContainer"
        return AppFindElement.find_element_by_name(must_play_popup)

    # 必玩主标题
    @staticmethod
    def title_text_result():
        title_text = poco('com.sinyee.babybus.world:id/title_tv').get_text()
        return title_text

    # 必玩副标题
    @staticmethod
    def subtitle_text_result():
        subtitle_text = poco('com.sinyee.babybus.world:id/subtitle_tv').get_text()
        return subtitle_text

    # 下载按钮的标题
    @staticmethod
    def must_download_text():
        download_text = poco('com.sinyee.babybus.world:id/btn_tv').get_text()
        return download_text

    # 下载按钮
    @staticmethod
    def must_download_button():
        download_button = "com.sinyee.babybus.world:id/btn_tv"
        return AppFindElement.find_element_by_name(download_button)

    '''
    【旧】逻辑
    # 标题文本：必玩游戏
    @staticmethod
    def title_text_result():
        title_text = poco('com.sinyee.babybus.world:id/tvTitle').get_text()
        return title_text

    # 关闭按钮
    @staticmethod
    def page_close_icon():
        page_close_icon = "com.sinyee.babybus.world:id/ivClose"
        return AppFindElement.find_element_by_name(page_close_icon)

    # 下载按钮
    @staticmethod
    def game_download_button():
        game_download_button = "com.sinyee.babybus.world:id/tvDownload"
        return AppFindElement.find_element_by_name(game_download_button)

    # 选中的子包个数
    @staticmethod
    def mark_game_count():
        mark_game_count = poco('com.sinyee.babybus.world:id/tvGameCount').get_text()
        return mark_game_count

    # 选中框获取
    @staticmethod
    def game_panel_list():
        gameList = poco("com.sinyee.babybus.world:id/rvMain").child("android.widget.RelativeLayout")
        #return len(list(gameList))
        abc = []
        for i in range(0,len(list(gameList))):
            gamelist2 = gameList[i].child('com.sinyee.babybus.world:id/content').children()
            abc.append(len(list(gamelist2)))
        return abc

    # 第一个必玩子包啊
    @staticmethod
    def first_mustgame_index():
        appFindElement = AppFindElement()
        first_game_index = "com.sinyee.babybus.world:id/rvMain"
        first_game_result = appFindElement.find_element_by_name(first_game_index)
        first_game_name = "android.widget.RelativeLayout"
        return first_game_result.child(first_game_name)[0]

    # 必玩子包索引
    @staticmethod
    def must_game_index(i):
        appFindElement = AppFindElement()
        must_game_index = "com.sinyee.babybus.world:id/rvMain"
        must_game_result = appFindElement.find_element_by_name(must_game_index)
        must_game_name = "android.widget.RelativeLayout"
        return must_game_result.child(must_game_name)[i]

    # 不可点击的 下载按钮
    @staticmethod
    def unable_download_button():
        unable_download_button = "com.sinyee.babybus.world:id/alDownload"
        return AppFindElement.find_element_by_name(unable_download_button).attr('enabled')

    # 自动播放弹窗
    @staticmethod
    def auto_play_panel():
        auto_play_panel = "com.sinyee.babybus.world:id/rlBg"
        return AppFindElement.find_element_by_name(auto_play_panel)

    '''
