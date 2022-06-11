# -*-coding:utf-8 -*-
from common.app.app_assert_lib import AppAssert
from test_data.base_data import *
from common.app_world.mange_world_panda import ManagePandaWorld

__author__ = 'WLX'

#  国内世界
class TestPandaWorldFlow(ManagePandaWorld,AppAssert):

    @classmethod
    def setUpClass(cls):
       cls.searchContent = PandaWorld.searchContent.value


    def setUp(self):
        self.launch_app()

    '''
    # 测试搜索能力
    def test_search_flow_class(self):

        #self.into_home_page()

        #进入搜索页
        self.into_search_page()
        # 搜索页进入子包
        self.search_intoapp_page()
        # 热搜
        self.hot_search_page()
        # 正常搜索
        self.valid_search_page()
        # 搜索无效词
        self.invalid_search_page()

    
    # 测试帮助反馈的能力
    def test_feedback_flow_class(self):

        self.default_faq_page()
        self.key_word_search_page()
        self.invalid_word_search_page()
        self.push_feedback_page()
        self.qq_online_page()
        self.img_contact_fun()
    '''
    # 测试空间清理的能力
    def test_space_manage_class(self):

        self.app_delete_fun()

    def tearDown(self):
        print('good')
        #self.stop_app()

