# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端-空间管理页--元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 空间管理页元素管理
class SpaceManagePageElement:

    # 子包 复选框
    @staticmethod
    def app_check_box():
        app_check_box = "com.sinyee.babybus.world:id/cb_son_package"
        return AppFindElement.find_element_by_name(app_check_box)

    # 删除按钮
    @staticmethod
    def app_delete_button():
        app_delete_button = "com.sinyee.babybus.world:id/tv_delete"
        return AppFindElement.find_element_by_name(app_delete_button)

    #二次确认框 确认按钮
    @staticmethod
    def delete_confirm_button():
        delete_confirm_button = "com.sinyee.babybus.world:id/tv_confirm"
        return AppFindElement.find_element_by_name(delete_confirm_button)

    #二次确认框 取消按钮
    @staticmethod
    def delete_cancel_button():
        delete_cancel_button = "com.sinyee.babybus.world:id/tv_cancel"
        return AppFindElement.find_element_by_name(delete_cancel_button)

    #空数据页面
    @staticmethod
    def no_data_tip():
        no_data_tip = "com.sinyee.babybus.world:id/iv_no_data_tip"
        return AppFindElement.find_element_by_name(no_data_tip)








    # 返回节点的个数
    @staticmethod
    def word_search_list():
        resultList = poco("com.sinyee.babybus.world:id/fl_fragment").child("android.widget.FrameLayout").child('android.widget.RelativeLayout').children()
        return len(list(resultList))
        #for i in range(0,len(list(menuList1))):
        #    return menuList1[i]



    # 遇到的问题，默认选择 其他
    @staticmethod
    def occur_question_item():
        appFindElement = AppFindElement()
        question_list_index = "com.sinyee.babybus.world:id/rl_list"
        question_list_item = appFindElement.find_element_by_name(question_list_index)
        question_name = "android.widget.RelativeLayout"
        return question_list_item.child(question_name)[5]



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