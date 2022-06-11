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
        self.launch_app()

    # 必玩翻译
    def testCase0_must_play_translation(self):
        # zh-CN: 1  en: 2 葡萄牙：9 西班牙：10
        self.must_play_popup_translation(1)

    # 关闭必玩
    def testCase1_close_must_play(self):
        self.verify_must_play_popup()


    def tearDown(self):
        #self.clear_app()
        pass

