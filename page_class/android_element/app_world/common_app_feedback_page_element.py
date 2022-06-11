# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端-帮助反馈页--元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 反馈帮助页元素管理
class FeedbackPageElement:

    # 默认FAQ，第一个词条
    @staticmethod
    def default_faq_index():
        appFindElement = AppFindElement()
        default_faq_index = "com.sinyee.babybus.world:id/lv_help"
        default_faq_item = appFindElement.find_element_by_name(default_faq_index)
        first_faq_name = "com.sinyee.babybus.world:id/rl_item"
        return default_faq_item.child(first_faq_name)[0]

    # 默认FAQ，第一个词条对应的答案
    @staticmethod
    def default_faq_answer():
        appFindElement = AppFindElement()
        default_faq_answer = "com.sinyee.babybus.world:id/lv_help"
        default_faq_answer_item = appFindElement.find_element_by_name(default_faq_answer)
        first_answer_name = "android.widget.RelativeLayout"
        return default_faq_answer_item.child(first_answer_name)[0]

    # 搜索页-输入框
    @staticmethod
    def world_search_input():
        world_search_input = "com.sinyee.babybus.world:id/et_search"
        return AppFindElement.find_element_by_name(world_search_input)


    # 搜索页-搜索结果-标题
    @staticmethod
    def word_search_title():
        word_title = poco('com.sinyee.babybus.world:id/tv_title').get_text()
        return word_title

    # 搜索页-搜索结果-内容
    @staticmethod
    def word_search_context():
        word_context = poco('com.sinyee.babybus.world:id/tv_context').get_text()
        return word_context

    # 返回节点的个数
    @staticmethod
    def word_search_list():
        resultList = poco("com.sinyee.babybus.world:id/fl_fragment").child("android.widget.FrameLayout").child('android.widget.RelativeLayout').children()
        return len(list(resultList))
        #for i in range(0,len(list(menuList1))):
        #    return menuList1[i]

    # 提交问题反馈按钮
    @staticmethod
    def into_question_button():
        into_question_button = "com.sinyee.babybus.world:id/btn_feedback_about"
        return AppFindElement.find_element_by_name(into_question_button)

    # 遇到的问题，默认选择 其他
    @staticmethod
    def occur_question_item():
        appFindElement = AppFindElement()
        question_list_index = "com.sinyee.babybus.world:id/rl_list"
        question_list_item = appFindElement.find_element_by_name(question_list_index)
        question_name = "android.widget.RelativeLayout"
        return question_list_item.child(question_name)[5]

    # 意见反馈区，选了‘其他’ 会弹意见反馈区
    @staticmethod
    def other_suggestion_area():
        other_suggestion_area = "com.sinyee.babybus.world:id/et_suggest"
        return AppFindElement.find_element_by_name(other_suggestion_area)

    # 手机号输入区
    @staticmethod
    def phone_num_area():
        phone_num_area = "com.sinyee.babybus.world:id/et_phone"
        return AppFindElement.find_element_by_name(phone_num_area)

    # 提交问题反馈按钮
    @staticmethod
    def submit_question_button():
        submit_question_button = "com.sinyee.babybus.world:id/tv_confirm"
        return AppFindElement.find_element_by_name(submit_question_button)

    # QQ群在线咨询
    @staticmethod
    def online_ask_button():
        online_ask_button = "com.sinyee.babybus.world:id/btn_feedback_qq"
        return AppFindElement.find_element_by_name(online_ask_button)

    # qq二维码
    @staticmethod
    def qq_feedback_text():
        qq_feedback_text = "用户反馈群"
        return AppFindElement.find_element_by_text(qq_feedback_text)

    # qq二维码弹窗关闭按钮
    @staticmethod
    def qq_feedback_close():
        qq_feedback_close = "com.sinyee.babybus.world:id/iv_close"
        return AppFindElement.find_element_by_name(qq_feedback_close)

    # 提交成功
    @staticmethod
    def submit_success_text():
        submit_success_text = "提交成功"
        return AppFindElement.find_element_by_text(submit_success_text)

    # 返回帮助反馈
    @staticmethod
    def back_feedback_button():
        back_feedback_button = "com.sinyee.babybus.world:id/btn_back_feedback_about"
        return AppFindElement.find_element_by_name(back_feedback_button)

    # 搜索页-返回按钮
    @staticmethod
    def search_back_button():
        search_back_button = "com.sinyee.babybus.world:id/llBack"
        return AppFindElement.find_element_by_name(search_back_button)

    # 热搜：第一个 热搜词
    @staticmethod
    def hot_search_index():
        appFindElement = AppFindElement()
        hot_search_index = "com.sinyee.babybus.world:id/lv"
        hot_search_security = appFindElement.find_element_by_name(hot_search_index)
        hotsearch_name = "android.widget.LinearLayout"
        return hot_search_security.child(hotsearch_name)[0]

    # 搜索页-热搜词
    @staticmethod
    def hot_search_word():
        hot_word = poco('com.sinyee.babybus.world:id/lv').child('android.widget.LinearLayout').child('com.sinyee.babybus.world:id/tvName').get_text()
        return hot_word

    # 搜索页 右侧默认第一个子包
    @staticmethod
    def default_app_index():
        appFindElement = AppFindElement()
        default_app_index = "com.sinyee.babybus.world:id/rv"
        default_app_item = appFindElement.find_element_by_name(default_app_index)
        default_name = "android.widget.RelativeLayout"
        return default_app_item.child(default_name)[0]

    # 右下角 联系合集
    @staticmethod
    def img_contact_button():
        img_contact_button = "com.sinyee.babybus.world:id/img_contact"
        return AppFindElement.find_element_by_name(img_contact_button)

    # qq群二维码
    @staticmethod
    def qq_group_button():
        qq_group_button = "com.sinyee.babybus.world:id/iv_qqgroup"
        return AppFindElement.find_element_by_name(qq_group_button)

    # 微信二维码
    @staticmethod
    def we_chat_button():
        we_chat_button = "com.sinyee.babybus.world:id/iv_wechat"
        return AppFindElement.find_element_by_name(we_chat_button)

    # 邮箱
    @staticmethod
    def baby_mail_button():
        baby_mail_button = "com.sinyee.babybus.world:id/iv_babybus"
        return AppFindElement.find_element_by_name(baby_mail_button)