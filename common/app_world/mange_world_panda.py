# coding=utf-8

__author__ = 'wlx'

import sys
from common.app.app_driver import AppDriver
from common.app_login import AppLogin
from common.app_world.pub_world_home_page import PubIntoHomePage
from common.app_world.pub_world_search import PubIntoSearchPage
from common.app_world.pub_world_package import PubIntoPackagePage
from common.app_world.pub_world_video import PubIntoVideoPage
from common.app_world.pub_world_feedback import PubIntoFeedbackPage
from common.app_world.pub_world_space_manage import PubMangeSpacePage

class ManagePandaWorld:

    #启动app
    def launch_app(self):
        try:
            app_driver = AppDriver()
            driver = app_driver.device_connect()
            app_driver.start_app_by_android('com.sinyee.babybus.world')
            return driver
        except AssertionError as e:
            print("error_info", e)

    #关闭app
    def stop_app(self):
        try:
            app_driver = AppDriver()
            driver = app_driver.device_connect()
            app_driver.stop_app_by_android('com.sinyee.babybus.world')
            return driver
        except AssertionError as e:
            print("error_info", e)

    # 登录
    def login(self):
        try:
            app_login = AppLogin()
            app_login.app_login()
        except AssertionError as e:
            print("error_info", e)

    # 进入主页
    def into_home_page(self):

        try:
            IntoHomePage = PubIntoHomePage()
            IntoHomePage.into_app_home_page()
        except AssertionError as e:
            print("error_info", e)

    # 0、进入搜索页
    def into_search_page(self):

        try:
            IntoSearchPage = PubIntoHomePage()
            IntoSearchPage.into_app_search_page()
        except AssertionError as e:
            print("error_info", e)

    # 1、常规词搜索
    def valid_search_page(self):

        try:
            IntoSearchPage = PubIntoSearchPage()
            IntoSearchPage.into_app_search_page()
        except AssertionError as e:
            print("error_info", e)

    # 2、无效词搜索
    def invalid_search_page(self):

        try:
            IntoSearchPage = PubIntoSearchPage()
            IntoSearchPage.into_app_empty_page()
        except AssertionError as e:
            print("error_info", e)

    # 3、热搜
    def hot_search_page(self):

        try:
            IntoSearchPage = PubIntoSearchPage()
            IntoSearchPage.app_hotsearch_page()
        except AssertionError as e:
            print("error_info", e)

    # 4、搜索页进入子包
    def search_intoapp_page(self):

        try:
            IntoSearchPage = PubIntoSearchPage()
            IntoSearchPage.search_into_app_page()
        except AssertionError as e:
            print("error_info", e)

    # 帮助反馈：1、默认词条选择
    def default_faq_page(self):

        try:
            IntoSearchPage = PubIntoFeedbackPage()
            IntoSearchPage.default_faq_page()
        except AssertionError as e:
            print("error_info", e)

    # 帮助反馈：2、关键字搜索
    def key_word_search_page(self):

        try:
            IntoSearchPage = PubIntoFeedbackPage()
            IntoSearchPage.key_word_search_page()
        except AssertionError as e:
            print("error_info", e)

    # 帮助反馈：3、无效词搜索
    def invalid_word_search_page(self):

        try:
            IntoSearchPage = PubIntoFeedbackPage()
            IntoSearchPage.invalid_word_search_page()
        except AssertionError as e:
            print("error_info", e)

    # 帮助反馈：4、提交问题反馈
    def push_feedback_page(self):

        try:
            IntoSearchPage = PubIntoFeedbackPage()
            IntoSearchPage.push_feedback_page()
        except AssertionError as e:
            print("error_info", e)

    # 帮助反馈：5、QQ群在线咨询
    def qq_online_page(self):

        try:
            IntoSearchPage = PubIntoFeedbackPage()
            IntoSearchPage.qq_online_chat_fun()
        except AssertionError as e:
            print("error_info", e)

    # 帮助反馈：6、联系集合（右下角）
    def img_contact_fun(self):

        try:
            IntoSearchPage = PubIntoFeedbackPage()
            IntoSearchPage.img_contact_fun()
        except AssertionError as e:
            print("error_info", e)

    # 空间管理：1、已下载App清理
    def app_delete_fun(self):

        try:
            MangeSpacePage = PubMangeSpacePage()
            MangeSpacePage.download_app_page()
        except AssertionError as e:
            print("error_info", e)

    # 默认子包、入口->返回
    def into_package_page(self):

        try:
            IntoPackagePage = PubIntoPackagePage()
            IntoPackagePage.into_app_package_page()
        except AssertionError as e:
            print("error_info", e)

    # 视频页操作
    def into_video_page(self):

        try:
            IntoVideoPage = PubIntoVideoPage()
            IntoVideoPage.into_app_video_page()
        except AssertionError as e:
            print("error_info", e)

    '''
    # 进入微博列表页面
    def into_page_list(self):
        try:
            # 进入微博列表
            IntoWeiboPageList = PubIntoPageListInfo()
            IntoWeiboPageList.into_page_list_info()
        except AssertionError as e:
            print("error_info", e)

    # 微博录入
    def write_weibo_page(self):
        try:
            # 微博录入
            WriteWeiboInfo = PubWriteWeiboInfo()
            WriteWeiboInfo.write_weibo_info()
        except AssertionError as e:
            print("error_info", e)

    # 微博详情页管理
    def weibo_detail_page(self):
        try:
            #
            DetailPageInfo = PubWeiboDetailPageInfo()
            DetailPageInfo.weibo_detail_page_info()
        except AssertionError as e:
            print("error_info", e)
    '''
