# -*- encoding=utf8 -*-
__author__ = "HB"
#移动端-等待
from airtest.core.api import *

class AppWait:
    '''
    :param time: 等待时间
    :return: 无
    '''
    #强制等待
    @staticmethod
    def wait(time):
        try:
            sleep(time)
        except AssertionError as e:
            print("error_info:",e)

    '''
    :param imgPath: 等待加载图形的相对路径，格式：r"相对路径"
    :return: None
    '''
    #等待图形加载
    @staticmethod
    def img_wait(imgPath):
        try:
            wait(Template(imgPath),timeout=20,interval=0.5)
        except TargetNotFoundError as e:
            print("error_info:",e)