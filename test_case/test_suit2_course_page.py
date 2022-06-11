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
       #cls.needhelpContent = PandaWorld.searchContent.value

    def setUp(self):
        #self.launch_app()
        pass


    # 首页测试流程
    def testCase1_into_course_page(self):

        self.into_course_page_fun()

    def tearDown(self):
        #self.clear_app()
        pass
        #self.stop_app()

