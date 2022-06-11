# -*- encoding=utf8 -*-

__author__ = "WLX"
#android端-帮助反馈页
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from page_class.android_element.app_world.common_app_feedback_page_element import FeedbackPageElement
from page_class.android_action.common_page_action import CommonPageAction
from common.app.app_wait import *
from common.app.app_assert_lib import *
from test_data.base_data import PandaWorld
from img.android_ui_img.app_world_page_img.world_page_img_manage import ManageWorldPageImg
from airtest.core.cv import Template


# 搜索类，管理帮助反馈相关的能力
class PubIntoFeedbackPage(AppAssert):

    # 1、默认词条选择
    def default_faq_page(self):

        # 点击第一个默认词条
        try:
            #点击第一默认词条
            default_faq_index = FeedbackPageElement.default_faq_index()
            if default_faq_index != None:
                is_default_faq_index_exists = True
            else:
                is_default_faq_index_exists = False
            self.assert_equal(is_default_faq_index_exists, True, "验证默认FQA词条是否存在")
            CommonPageAction.click(default_faq_index)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 验证词条对应的答案是否存在
        try:
            default_faq_answer = FeedbackPageElement.default_faq_answer()
            if default_faq_answer != None:
                is_default_faq_answer_exists = True
            else:
                is_default_faq_answer_exists = False
            self.assert_equal(is_default_faq_answer_exists, True, "验证FAQ结果是否存在")
        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)

    # 2、关键字搜索
    def key_word_search_page(self):

        # 输入关键字 + 搜索
        try:
            world_search_input = FeedbackPageElement.world_search_input()
            if world_search_input != None:
                is_world_search_input_exists = True
            else:
                is_world_search_input_exists = False
            self.assert_equal(is_world_search_input_exists, True, "验证搜索输入框是否存在")
            CommonPageAction.input(world_search_input, PandaWorld.searchFeedback.value)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 搜索结果校验
        try:
            word_search_title = FeedbackPageElement.word_search_title()
            word_search_context = FeedbackPageElement.word_search_context()
            if PandaWorld.searchFeedback.value in word_search_title and PandaWorld.searchFeedback.value in word_search_context :
                is_word_search_result_exists = True
            else:
                is_word_search_result_exists = False
            self.assert_equal(is_word_search_result_exists, True, "验证搜索结果是否正确")

        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)


    # 3、无效词搜索
    def invalid_word_search_page(self):

        # 输入无效关键字 + 搜索
        try:
            world_search_input = FeedbackPageElement.world_search_input()
            CommonPageAction.input(world_search_input, PandaWorld.invalid_feedback_Content.value)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 搜索结果页--通过标题是否存在来判断结果
        try:
            word_search_list = FeedbackPageElement.word_search_list()
            # 通过节点 判断搜索结果，如果有结果，节点会增加1个
            if word_search_list == 4 :
                is_word_search_result_exists = True
            else:
                is_word_search_result_exists = False
            self.assert_equal(is_word_search_result_exists, True, "验证搜索结果是否正确")

        except AssertionError as e:
            print("error_info", e)
            AppWait.wait(3)

    # 4、提交问题反馈
    def push_feedback_page(self):

        # 提交问题反馈
        try:
            into_question_button = FeedbackPageElement.into_question_button()
            if into_question_button != None:
                is_into_question_button_exists = True
            else:
                is_into_question_button_exists = False
            self.assert_equal(is_into_question_button_exists, True, "验证提交问题反馈的入口是否存在")
            CommonPageAction.click(into_question_button)
            AppWait.wait(2)
        except AssertionError as e:
            print("error_info", e)

        # 遇到的问题类型，选 ‘其他’
        try:
            occur_question_item = FeedbackPageElement.occur_question_item()
            if occur_question_item != None:
                is_occur_question_item_exists = True
            else:
                is_occur_question_item_exists = False
            self.assert_equal(is_occur_question_item_exists, True, "验证问题类型选项是否存在")
            CommonPageAction.click(occur_question_item)
            AppWait.wait(2)
        except AssertionError as e:
            print("error_info", e)

        # 意见区 输入
        try:
            other_suggestion_area = FeedbackPageElement.other_suggestion_area()
            CommonPageAction.input(other_suggestion_area, PandaWorld.suggestion.value)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 手机号 输入
        try:
            phone_num_area = FeedbackPageElement.phone_num_area()
            CommonPageAction.input(phone_num_area, PandaWorld.phone_num.value)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 提交按钮
        try:
            submit_question_button = FeedbackPageElement.submit_question_button()
            CommonPageAction.click(submit_question_button)
            AppWait.wait(2)
        except AssertionError as e:
            print("error_info", e)

        # 验证提交结果并返回列表
        try:
            submit_success_text = FeedbackPageElement.submit_success_text()
            if submit_success_text != None:
                is_submit_success_text_exists = True
            else:
                is_submit_success_text_exists = False
            self.assert_equal(is_submit_success_text_exists, True, "验证是否提交成功")
            back_feedback_button = FeedbackPageElement.back_feedback_button()
            CommonPageAction.click(back_feedback_button)
            AppWait.wait(2)
        except AssertionError as e:
            print("error_info", e)


        # 物理 返回 搜索页
        #CommonPageAction.keyboard_click("BACK")
        #keyevent("BACK")
            
    # 5、QQ群在线咨询
    def qq_online_chat_fun(self):

        # 点击入口按钮
        try:
            online_ask_button = FeedbackPageElement.online_ask_button()
            CommonPageAction.click(online_ask_button)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 弹出二维码
        try:
            qq_feedback_text = FeedbackPageElement.qq_feedback_text()
            if qq_feedback_text != None:
                is_qq_feedback_text_exists = True
            else:
                is_qq_feedback_text_exists = False
            self.assert_equal(is_qq_feedback_text_exists, True, "验证是否提交成功")
            qq_feedback_close = FeedbackPageElement.qq_feedback_close()
            CommonPageAction.click(qq_feedback_close)
            AppWait.wait(2)
        except AssertionError as e:
            print("error_info", e)

    # 6、联系方式合集
    def img_contact_fun(self):

        # 点击右下角 联系方式合集
        try:
            img_contact_button = FeedbackPageElement.img_contact_button()
            if img_contact_button != None:
                is_img_contact_button_exists = True
            else:
                is_img_contact_button_exists = False
            self.assert_equal(is_img_contact_button_exists, True, "验证联系方式集合入口是否存在")
            CommonPageAction.click(img_contact_button)
            AppWait.wait(3)
        except AssertionError as e:
            print("error_info", e)

        # 弹出二维码合集
        try:
            qq_group_button = FeedbackPageElement.qq_group_button()
            we_chat_button = FeedbackPageElement.we_chat_button()
            baby_mail_button = FeedbackPageElement.baby_mail_button()
            if qq_group_button != None and we_chat_button != None and baby_mail_button != None:
                is_qr_code__exists = True
            else:
                is_qr_code__exists = False
            self.assert_equal(is_qr_code__exists, True, "验证是否二维码是否存在")
            AppWait.wait(2)
            # 物理 返回 搜索页
            CommonPageAction.keyboard_click("BACK")
        except AssertionError as e:
            print("error_info", e)