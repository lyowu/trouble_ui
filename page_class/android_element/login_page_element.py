# -*- encoding=utf8 -*-
__author__ = "WLX"
#android端- 登录页面-元素
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from common.app.app_find_element import AppFindElement
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

class LoginPageElement:
    #手机号输入
    @staticmethod
    def mobile_account_input():
        mobile_account_input = "com.nd.app.factory.goodquestion:id/et_account_first"
        return AppFindElement.find_element_by_name(mobile_account_input)

    #手机登录密码
    @staticmethod
    def mobile_pwd_input():
        mobile_pwd_input = "com.nd.app.factory.goodquestion:id/et_password"
        return AppFindElement.find_element_by_name(mobile_pwd_input)

    #协议
    @staticmethod
    def protocol_radio():
        protocol_radio = "com.nd.app.factory.goodquestion:id/cb_protocol"
        return AppFindElement.find_element_by_name(protocol_radio)

    #登录按钮
    @staticmethod
    def login_button():
        login_button = "com.nd.app.factory.goodquestion:id/btn_complete"
        return AppFindElement.find_element_by_name(login_button)