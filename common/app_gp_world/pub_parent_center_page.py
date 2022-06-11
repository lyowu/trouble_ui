# -*- encoding=utf8 -*-

__author__ = "WLX"
#android端- 家长中心页
import re
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from page_class.android_element.app_world_google.common_app_parent_center_element import ParentCenterPageElement
from page_class.android_action.app_world_google.common_page_action import CommonPageAction
from common.app_gp_world.pub_excel_data_value import PubExcelOperator
from common.app.app_wait import *
from common.app.app_assert_lib import *
from airtest.core.cv import Template
from test_data.base_data import PandaWorld

# 家长中心页
class PubIntoParentPage(AppAssert):

    # 家长中心页 翻译
    def parent_center_translation(self,excel_Column):

        try:
            # 参数：对应列的值，1是第2列，可以指定对应的列
            # zh-CN: 1  en: 2
            excel_list = PubExcelOperator.get_excel_value(excel_Column)
            AppWait.wait(2)
            #print(excel_list)
            element_list = []

            # 空间管理
            space_management_text = ParentCenterPageElement.space_management_text()
            #print(space_management_text)
            element_list.append(space_management_text)

            # 已下载APP
            downloaded_games_text = ParentCenterPageElement.downloaded_games_text()
            element_list.append(downloaded_games_text)
            #print(downloaded_games_text)

            # 视频缓存
            downloaded_videos_text = ParentCenterPageElement.downloaded_videos_text()
            element_list.append(downloaded_videos_text)
            #print(downloaded_videos_text)

            ### 已下载子包复选框，勾选
            downloaded_games_checkbox = ParentCenterPageElement.downloaded_games_checkbox()
            CommonPageAction.click(downloaded_games_checkbox)
            AppWait.wait(1)

            # 删除
            tv_delete_text = ParentCenterPageElement.tv_delete_text()
            element_list.append(tv_delete_text)

            ### 点击删除按钮
            tv_delete_button = ParentCenterPageElement.tv_delete_button()
            CommonPageAction.click(tv_delete_button)
            AppWait.wait(1)

            # 确认要删除选中内容吗？
            delete_note_text = ParentCenterPageElement.delete_note_text()
            # 判断中英文的括号，返回Ture和False
            is_note_text = '（' in delete_note_text
            if is_note_text == True:
                # 括号的索引，中文字符
                ind = delete_note_text.index('（')
            else:
                # 括号的索引，英文字符
                ind = delete_note_text.index('(')

            # 需要截取字符串 （xxxMb）不做对比
            delete_note = delete_note_text[:ind]
            element_list.append(delete_note)

            ### 点击【取消】按钮
            tv_cancel_button = ParentCenterPageElement.tv_cancel_button()
            CommonPageAction.click(tv_cancel_button)
            AppWait.wait(1)

            # 设置
            setting_text_result = ParentCenterPageElement.setting_text_result()
            element_list.append(setting_text_result)

            ### 点设置，切到设置页
            setting_name_result = ParentCenterPageElement.setting_name_result()
            CommonPageAction.click(setting_name_result)
            AppWait.wait(1)

            # 护眼模式
            eye_saver_text = ParentCenterPageElement.eye_saver_text()
            element_list.append(eye_saver_text)

            # 使用时长设置
            use_time_control = ParentCenterPageElement.use_time_control()
            element_list.append(use_time_control)

            ### 海外默认使用时长是关闭，要打开
            use_time_switch = ParentCenterPageElement.use_time_switch()
            CommonPageAction.click(use_time_switch)
            AppWait.wait(1)

            # 每次使用时长
            each_use_time = ParentCenterPageElement.each_use_time()
            element_list.append(each_use_time)

            # 每次休息时长
            each_rest_time = ParentCenterPageElement.each_rest_time()
            element_list.append(each_rest_time)

            # 流量保护
            data_traffic_protect = ParentCenterPageElement.data_traffic_protect()
            element_list.append(data_traffic_protect)

            # 滚动下翻
            poco("android.widget.ScrollView").swipe([-0.1, -0.6])
            AppWait.wait(3)

            # 使用流量时需验证
            confirm_before_usage = ParentCenterPageElement.confirm_before_usage()
            element_list.append(confirm_before_usage)

            # 使用流量时不需要验证
            noconfirm_before_usage = ParentCenterPageElement.noconfirm_before_usage()
            element_list.append(noconfirm_before_usage)

            # 播放语音提示
            play_voice_prompt = ParentCenterPageElement.play_voice_prompt()
            element_list.append(play_voice_prompt)

            # 播放背景音乐
            play_bg_music = ParentCenterPageElement.play_bg_music()
            element_list.append(play_bg_music)

            # 下载完成后开始游戏
            auto_play_game = ParentCenterPageElement.auto_play_game()
            element_list.append(auto_play_game)

            #print(element_list)

            if element_list == excel_list:
                is_space_management_text_exists = True
            else:
                is_space_management_text_exists = False

                # 对比2个List的区别
                defferent_list = set(element_list).difference(set(excel_list))
                print('跟文档不一致的选项：', defferent_list)
            self.assert_equal(is_space_management_text_exists, True, "验证翻译是否正确")

            AppWait.wait(3)

        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

    # FAQ
    def parent_center_faq(self):

        try:
            # 点击FAQ
            faq_access_button = ParentCenterPageElement.faq_access_button()
            CommonPageAction.click(faq_access_button)
            AppWait.wait(1)

            help_list_index = ParentCenterPageElement.help_list_index()
            for i in range(0, len(list(help_list_index))-1):
                # 获取每一条帮助的标题
                help_item_name = ParentCenterPageElement.help_item_name(i)
                CommonPageAction.click(help_list_index[i])
                AppWait.wait(1)
                # 获取每一条帮助的内容
                help_context = ParentCenterPageElement.help_context_detail()
                AppWait.wait(1)
                # 验证标题和内容是否为空
                if help_item_name is None and help_context is None:
                    is_help_item_text_exists = True
                else:
                    is_help_item_text_exists = False
                self.assert_equal(is_help_item_text_exists, False, "验证FAQ内容是否存在")
                # 关闭标题，并且往下滑，因为到【我已订阅xxx】会把上面的顶上去，导致索引计数错误，所以每次都要回到顶部
                CommonPageAction.click(help_list_index[i])
                poco("com.sinyee.babybus.world:id/lv_help").swipe([0.1, 0.6])
                AppWait.wait(1)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

    # 反馈功能 -差评
    def parent_center_bad_feedback(self):

        try:
            # 点击右下角反馈
            feedback_access_button = ParentCenterPageElement.feedback_access_button()
            CommonPageAction.click(feedback_access_button)
            AppWait.wait(1)

            # 点击2颗星，触发反馈
            feedback_star1_icon = ParentCenterPageElement.feedback_star1_icon()
            if feedback_star1_icon != None:
                is_feedback_star1_icon_exists = True
            else:
                is_feedback_star1_icon_exists = False
            self.assert_equal(is_feedback_star1_icon_exists, True, "验证评论星星是否存在")
            CommonPageAction.click(feedback_star1_icon)
            AppWait.wait(1)

            # 内容输入
            feedback_input_area = ParentCenterPageElement.feedback_input_area()
            CommonPageAction.input(feedback_input_area, PandaWorld.feedback.value)
            AppWait.wait(1)
            # 获取当前的字数
            current_feedback_num = ParentCenterPageElement.current_feedback_num()
            if int(current_feedback_num) == len(PandaWorld.feedback.value):
                is_feedback_num_correctly = True
            else:
                is_feedback_num_correctly = False
            self.assert_equal(is_feedback_num_correctly, True, "验证输入内容跟面板统计是否一致")

            # 提交反馈
            feedback_submit_button = ParentCenterPageElement.feedback_submit_button()
            CommonPageAction.click(feedback_submit_button)

        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

    # 反馈功能 -好评
    def parent_center_best_feedback(self):

        try:
            # 点击右下角反馈
            feedback_access_button = ParentCenterPageElement.feedback_access_button()
            CommonPageAction.click(feedback_access_button)
            AppWait.wait(1)

            # 点击5颗星，跳到商城
            feedback_star4_icon = ParentCenterPageElement.feedback_star4_icon()
            CommonPageAction.click(feedback_star4_icon)
            AppWait.wait(2)
            # 物理返回，到家长空间
            keyevent("BACK")
            AppWait.wait(2)
        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)

    # 设置
    def parent_center_setting_fun(self):

        try:
            # 设置入口
            setting_name_result = ParentCenterPageElement.setting_name_result()
            CommonPageAction.click(setting_name_result)
            AppWait.wait(1)

            # 护眼模式 开关 打开
            eye_saver_switch = ParentCenterPageElement.eye_saver_switch()
            CommonPageAction.click(eye_saver_switch)
            AppWait.wait(1)

            # 获取蒙层
            eye_saver_view = ParentCenterPageElement.eye_saver_view()
            if eye_saver_view != None:
                is_eye_saver_view_exists = True
            else:
                is_eye_saver_view_exists = False
            self.assert_equal(is_eye_saver_view_exists, True, "验证护眼蒙层是否存在")

            # 护眼模式 关闭
            CommonPageAction.click(eye_saver_switch)
            # 翻到最底下
            poco("android.widget.ScrollView").swipe([-0.1, -0.8])
            AppWait.wait(1)
            poco("android.widget.ScrollView").swipe([-0.1, -0.8])
            AppWait.wait(1)

            # 隐私政策
            user_privacy_agreement = ParentCenterPageElement.user_privacy_agreement()
            CommonPageAction.click(user_privacy_agreement)
            AppWait.wait(1)
            keyevent("BACK")
            AppWait.wait(1)

            # 用户协议
            member_rights_agreement = ParentCenterPageElement.member_rights_agreement()
            CommonPageAction.click(member_rights_agreement)
            AppWait.wait(1)
            keyevent("BACK")
            AppWait.wait(1)

        except AssertionError as e:
            print("error_info", e)
        AppWait.wait(3)