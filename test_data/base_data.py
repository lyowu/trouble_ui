# -*- encoding=utf8 -*-
__author__ = "WLX"
# 测试-基础数据
from enum import Enum
import random

class TestEnv(Enum):
    # 移动端数据
    packageName='com.nd.app.factory.goodquestion'
    mobile_input = '13015728081'
    mobile_pwd = 'Abc123456'

    # WEB端数据
    url = 'https://manage-portal-web.beta.101.com/'
    account = '157745@EP_1537932799363'
    password = '123456'
    # 101平台
    url_101 = 'http://r.xue.101.com/auto_portal_app_180926114906/account/login'
    account_101 = '232350'
    password_101 = '123456'


# 国内世界
class PandaWorld(Enum):
    searchContent = '安全'
    invalidContent = '无效'
    searchFeedback = '下载'
    invalid_feedback_Content = '无效'
    suggestion = '测试'
    phone_num = '19959156688'
    feedback = '产品好用'
