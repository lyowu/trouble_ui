# -*- encoding=utf8 -*-
__author__ = "WLX"
# 家长中心
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 家长中心页元素管理
class ParentCenterPageElement:

    # 空间管理
    @staticmethod
    def space_management_text():
        space_management_text = poco('com.sinyee.babybus.world:id/rb_download').get_text()
        return space_management_text

    # 已下载APP
    @staticmethod
    def downloaded_games_text():
        downloaded_games_text = poco('com.sinyee.babybus.world:id/rg_titleTop').child('android.widget.LinearLayout').child('android.widget.LinearLayout')[0].child('android.widget.LinearLayout').child('android.widget.LinearLayout').child('com.sinyee.babybus.world:id/txt_title').get_text()
        return downloaded_games_text

    # 视频缓存
    @staticmethod
    def downloaded_videos_text():
        downloaded_videos_text = poco('com.sinyee.babybus.world:id/rg_titleTop').child('android.widget.LinearLayout').child('android.widget.LinearLayout')[1].child('android.widget.LinearLayout').child('android.widget.LinearLayout').child('com.sinyee.babybus.world:id/txt_title').get_text()
        return downloaded_videos_text

    # 已下载子包复选框
    @staticmethod
    def downloaded_games_checkbox():
        downloaded_games_checkbox = "com.sinyee.babybus.world:id/cb_son_package"
        return AppFindElement.find_element_by_name(downloaded_games_checkbox)

    # 删除 按钮
    @staticmethod
    def tv_delete_button():
        tv_delete_button = "com.sinyee.babybus.world:id/tv_delete"
        return AppFindElement.find_element_by_name(tv_delete_button)

    # 删除-文本
    @staticmethod
    def tv_delete_text():
        tv_delete_text = poco('com.sinyee.babybus.world:id/tv_delete').get_text()
        return tv_delete_text

    # 删除提示语-文本
    @staticmethod
    def delete_note_text():
        delete_note_text = poco('com.sinyee.babybus.world:id/tv_title').get_text()
        return delete_note_text

    # 取消 按钮
    @staticmethod
    def tv_cancel_button():
        tv_cancel_button = "com.sinyee.babybus.world:id/tv_cancel"
        return AppFindElement.find_element_by_name(tv_cancel_button)

    # 设置-文本
    @staticmethod
    def setting_text_result():
        setting_text = poco('com.sinyee.babybus.world:id/rb_setting').get_text()
        return setting_text

    # 设置按钮
    @staticmethod
    def setting_name_result():
        setting_name_result = "com.sinyee.babybus.world:id/rb_setting"
        return AppFindElement.find_element_by_name(setting_name_result)

    # 护眼模式
    @staticmethod
    def eye_saver_text():
        eye_saver_text = poco('com.sinyee.babybus.world:id/llEye').child('android.widget.LinearLayout').child('android.widget.TextView').get_text()
        return eye_saver_text

    # 护眼模式 开关
    @staticmethod
    def eye_saver_switch():
        eye_saver_switch = "com.sinyee.babybus.world:id/ivEye"
        return AppFindElement.find_element_by_name(eye_saver_switch)

    # 护眼模式 蒙层
    @staticmethod
    def eye_saver_view():
        eye_saver_view = "com.sinyee.babybus.world:id/eye_view"
        return AppFindElement.find_element_by_name(eye_saver_view)

    # 使用时长设置 标题
    @staticmethod
    def use_time_control():
        use_time_control = poco('com.sinyee.babybus.world:id/tv_everyday').get_text()
        return use_time_control

    # 使用时长设置 开关
    @staticmethod
    def use_time_switch():
        use_time_switch = "com.sinyee.babybus.world:id/iv_switch"
        return AppFindElement.find_element_by_name(use_time_switch)

    # 每次使用时长
    @staticmethod
    def each_use_time():
        each_use_time = poco('com.sinyee.babybus.world:id/tv_usetime').get_text()
        return each_use_time

    # 每次休息时长
    @staticmethod
    def each_rest_time():
        each_rest_time = poco('com.sinyee.babybus.world:id/tv_everyday_resttime').get_text()
        return each_rest_time

    # 流量保护
    @staticmethod
    def data_traffic_protect():
        data_traffic_protect = poco('android.widget.ScrollView').child('android.widget.LinearLayout').child('android.widget.LinearLayout').child('android.widget.LinearLayout').child('android.widget.TextView').get_text()
        return data_traffic_protect

    # 使用流量时需验证
    @staticmethod
    def confirm_before_usage():
        confirm_before_usage = poco('com.sinyee.babybus.world:id/rl_download_verify').child('android.widget.TextView').get_text()
        return confirm_before_usage

    # 使用流量时不需要验证
    @staticmethod
    def noconfirm_before_usage():
        noconfirm_before_usage = poco('com.sinyee.babybus.world:id/rl_download_no_verify').child('android.widget.TextView').get_text()
        return noconfirm_before_usage

    # 播放语音提示
    @staticmethod
    def play_voice_prompt():
        play_voice_prompt = poco('com.sinyee.babybus.world:id/llSound').child("android.widget.LinearLayout").child('android.widget.TextView').get_text()
        return play_voice_prompt

    # 播放背景音乐
    @staticmethod
    def play_bg_music():
        play_bg_music = poco('com.sinyee.babybus.world:id/llGoogleBgm').child("android.widget.LinearLayout").child('android.widget.TextView').get_text()
        return play_bg_music

    # 下载完成后开始游戏
    @staticmethod
    def auto_play_game():
        auto_play_game = poco('com.sinyee.babybus.world:id/llAutoPlay').child("android.widget.LinearLayout").child('android.widget.TextView').get_text()
        return auto_play_game

    # FAQ-左侧入口
    @staticmethod
    def faq_access_button():
        faq_access_button = "com.sinyee.babybus.world:id/rb_feedback"
        return AppFindElement.find_element_by_name(faq_access_button)

    # FAQ-右侧帮助列表
    @staticmethod
    def help_list_index():
        help_index = poco("com.sinyee.babybus.world:id/lv_help").children()
        return help_index

    # FAQ-右侧帮助列表名
    @staticmethod
    def help_item_name(i):
        help_item_name = poco('com.sinyee.babybus.world:id/lv_help').children()
        help_sub_name = help_item_name[i].child('com.sinyee.babybus.world:id/lin_ex_group').child('com.sinyee.babybus.world:id/tv_title').get_text()
        return help_sub_name

    # 帮助内容
    @staticmethod
    def help_context_detail():
        help_context_detail = poco('com.sinyee.babybus.world:id/tv_context').get_text()
        return help_context_detail

    ####
    # 右下角反馈入口
    @staticmethod
    def feedback_access_button():
        faq_access_button = "com.sinyee.babybus.world:id/rateBtn"
        return AppFindElement.find_element_by_name(faq_access_button)

    # 反馈 关闭按钮
    @staticmethod
    def feedback_close_button():
        feedback_close_button = "com.sinyee.babybus.world:id/rl_rate_bg"
        return AppFindElement.find_element_by_name(feedback_close_button)

    # 星星 -2颗星
    @staticmethod
    def feedback_star1_icon():
        feedback_star_icon = "com.sinyee.babybus.world:id/rl_rate_star1"
        return AppFindElement.find_element_by_name(feedback_star_icon)

    # 星星 -5颗星
    @staticmethod
    def feedback_star4_icon():
        feedback_star4_icon = "com.sinyee.babybus.world:id/rl_rate_star4"
        return AppFindElement.find_element_by_name(feedback_star4_icon)

    # 反馈输入区域
    @staticmethod
    def feedback_input_area():
        feedback_input_area = "com.sinyee.babybus.world:id/et_advice_text"
        return AppFindElement.find_element_by_name(feedback_input_area)

    # 当前字数
    @staticmethod
    def current_feedback_num():
        current_feedback_num = poco('com.sinyee.babybus.world:id/tv_advice_cur_length').get_text()
        return current_feedback_num

    # 反馈提交按钮
    @staticmethod
    def feedback_submit_button():
        feedback_submit_button = "com.sinyee.babybus.world:id/tv_btn_submit"
        return AppFindElement.find_element_by_name(feedback_submit_button)

    # 隐私政策
    @staticmethod
    def user_privacy_agreement():
        user_privacy_agreement = "com.sinyee.babybus.world:id/rl_user_privacy_agreement"
        return AppFindElement.find_element_by_name(user_privacy_agreement)

    # 用户协议
    @staticmethod
    def member_rights_agreement():
        member_rights_agreement = "com.sinyee.babybus.world:id/rl_member_rights_agreement"
        return AppFindElement.find_element_by_name(member_rights_agreement)