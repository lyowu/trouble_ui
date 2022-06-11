# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端-微博详情页--元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

class DetailPageElement:

    # weibo输入页面
    @staticmethod
    def weibo_favorite_icon():
        weibo_favorite_icon = "收藏"
        return AppFindElement.find_element_by_text(weibo_favorite_icon)

    # weibo 点赞
    @staticmethod
    def weibo_like_icon():
        weibo_like_icon = "赞"
        return AppFindElement.find_element_by_text(weibo_like_icon)


