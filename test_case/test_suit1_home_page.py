# -*-coding:utf-8 -*-
from common.app.app_assert_lib import AppAssert
from test_data.base_data import *
from common.app_gp_world.mange_world_google import ManageGoogleWorld

__author__ = 'WLX'

#  google world
class TestHomePageFlow(ManageGoogleWorld,AppAssert):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass
        #self.launch_app()

    # 关闭新品弹窗
    def testCase0_close_new_pop(self):
        self.close_new_pop_window()

    # 测试进入自带子包
    def testCase1_into_default_game(self):
        self.into_default_game_fun()

    # 测试顶部tab切换
    def testCase2_switch_tab_index(self):
        self.switch_tab_index_fun()

    # 测试进入视频页
    def testCase3_into_video(self):
        self.into_video_fun()

    # 测试计入子包，含下载  这个时候可能会有广告，需
    def testCase4_into_game(self):
        self.into_app_game_fun()


    def tearDown(self):
        #self.clear_app()
        pass

