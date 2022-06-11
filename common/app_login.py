# -*- encoding=utf8 -*-

from common.app.app_assert_lib import *
from common.app.app_wait import AppWait
from page_class.android_element.login_page_element import LoginPageElement
from page_class.android_action.login_page_action import LoginPageAction
from test_data.base_data import TestEnv
from common.app.app_driver import *

__author__ = 'WLX'

class AppLogin(AppAssert):
    # app登录
    def app_login(self):
        # 账号
        mobile_input=LoginPageElement.mobile_account_input()
        if mobile_input !=None:
            is_mobile_input_exists = True
        else:
            is_mobile_input_exists = False
        self.assert_equal(is_mobile_input_exists,True,"验证账号输入框是否存在")
        LoginPageAction.input(mobile_input,TestEnv.mobile_input.value)

        # 密码
        AppWait.wait(2)
        password_input=LoginPageElement.mobile_pwd_input()
        if password_input != None:
            is_password_input_exists = True
        else:
            is_password_input_exists = False
        self.assert_equal(is_password_input_exists,True,"验证密码输入框是否存在")
        LoginPageAction.input(password_input,TestEnv.mobile_pwd.value)

        # 协议
        AppWait.wait(2)
        protocol_radio=LoginPageElement.protocol_radio()
        if protocol_radio != None:
            is_protocol_radio_exists = True
        else:
            is_protocol_radio_exists = False
        self.assert_equal(is_protocol_radio_exists,True,"验证登录按钮是否存在")
        LoginPageAction.click(protocol_radio)
        AppWait.wait(3)

        # 登录按钮
        AppWait.wait(2)
        login_button=LoginPageElement.login_button()
        if login_button != None:
            is_login_button_exists = True
        else:
            is_login_button_exists = False
        self.assert_equal(is_login_button_exists,True,"验证登录按钮是否存在")
        LoginPageAction.click(login_button)
        AppWait.wait(3)




