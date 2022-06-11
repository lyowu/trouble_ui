# coding=utf-8

__author__ = 'wlx'

import sys
from common.app.app_driver import AppDriver
from common.app_login import AppLogin
from common.app_gp_world.pub_must_play_page import PubIntoMustPlayPage
from common.app_gp_world.pub_parent_center_page import PubIntoParentPage
from common.app_gp_world.pub_world_home_page import PubIntoHomePage


class ManageGoogleWorld:

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

    #清理app
    def clear_app(self):
        try:
            app_driver = AppDriver()
            driver = app_driver.device_connect()
            app_driver.clear_app_by_android('com.sinyee.babybus.world')
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

    # 家长中心页，翻译检查
    def into_parent_center_page(self,i):

        try:
            IntoParentPage = PubIntoParentPage()
            IntoParentPage.parent_center_translation(i)
        except AssertionError as e:
            print("error_info", e)

    # 家长中心页，FAQ
    def parent_center_faq_page(self):

        try:
            IntoParentPage = PubIntoParentPage()
            IntoParentPage.parent_center_faq()
        except AssertionError as e:
            print("error_info", e)

    # 家长中心页，差评触发 评价
    def parent_center_bad_feedback(self):

        try:
            IntoParentPage = PubIntoParentPage()
            IntoParentPage.parent_center_bad_feedback()
        except AssertionError as e:
            print("error_info", e)

    # 家长中心页，好评 跳商城
    def parent_center_best_feedback(self):

        try:
            IntoParentPage = PubIntoParentPage()
            IntoParentPage.parent_center_best_feedback()
        except AssertionError as e:
            print("error_info", e)

    # 家长中心页，设置-
    def parent_center_setting_flow(self):

        try:
            IntoParentPage = PubIntoParentPage()
            IntoParentPage.parent_center_setting_fun()
        except AssertionError as e:
            print("error_info", e)

    # 必玩页，翻译检查
    def must_play_popup_translation(self, i):

        try:
            MustPlayTranslation = PubIntoMustPlayPage()
            MustPlayTranslation.must_play_translation(i)
        except AssertionError as e:
            print("error_info", e)

    # 必玩页
    def verify_must_play_popup(self):

        try:
            IntoMustPlayPage = PubIntoMustPlayPage()
            IntoMustPlayPage.must_play_popup()
        except AssertionError as e:
            print("error_info", e)

    # 关闭新品弹窗
    def close_new_pop_window(self):

        try:
            IntoHomePage = PubIntoHomePage()
            # 关闭新品弹窗
            IntoHomePage.new_pop_window()

        except AssertionError as e:
            print("error_info", e)

    # 测试进默认子包
    def into_default_game_fun(self):

        try:
            IntoHomePage = PubIntoHomePage()
            # 进默认子包
            IntoHomePage.into_default_app_fun()

        except AssertionError as e:
            print("error_info", e)

    # 切换顶部tab
    def switch_tab_index_fun(self):

        try:
            IntoHomePage = PubIntoHomePage()
            # 切换顶部tab
            IntoHomePage.home_page_tab_switch()

        except AssertionError as e:
            print("error_info", e)

    # 进视频页（观看、返回）
    def into_video_fun(self):

        try:
            IntoHomePage = PubIntoHomePage()
            # 切换顶部tab
            IntoHomePage.into_specific_video_fun()

        except AssertionError as e:
            print("error_info", e)

    # 进子包页（下载、返回）
    def into_app_game_fun(self):

        try:
            IntoHomePage = PubIntoHomePage()
            # 切换顶部tab
            IntoHomePage.into_specific_app_fun()

        except AssertionError as e:
            print("error_info", e)

    # 进入课程
    def into_course_page_fun(self):

        try:
            IntoHomePage = PubIntoHomePage()
            #
            IntoHomePage.into_course_fun()

        except AssertionError as e:
            print("error_info", e)

