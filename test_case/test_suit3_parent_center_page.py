# -*-coding:utf-8 -*-
from common.app.app_assert_lib import AppAssert
from test_data.base_data import *
from common.app_gp_world.mange_world_google import ManageGoogleWorld

__author__ = 'WLX'

#  google world
class TestCoursePageFlow(ManageGoogleWorld,AppAssert):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        #self.launch_app()
        pass


    # 家长中心翻译
    def testCase1_parent_center_translation(self):
        # 参数：EXCEL里面对应列的值，1表示第2列 即中文，2表示第3列 即英文，以此类推，测什么语言切什么列
        # zh-CN: 1,  en: 2, zh-TW:3,
        self.into_parent_center_page(1)

    # 反馈 差评
    def testCase2_bad_feedback_flow(self):
        self.parent_center_bad_feedback()
        #pass

    # 反馈 好评
    def testCase3_best_feedback_flow(self):
        self.parent_center_best_feedback()
        #pass

    # FAQ
    def testCase4_faq_page(self):
        self.parent_center_faq_page()
        #pass

    def testCase5_setting_page(self):
        self.parent_center_setting_flow()

    def tearDown(self):
        #self.clear_app()
        pass
        #self.stop_app()

