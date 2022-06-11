# -*- encoding=utf8 -*-
__author__ = "WLX"
#移动端-驱动
from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.ios import *
from tidevice import Usbmux
#from poco.drivers.ios import iosPoco
#poco = iosPoco()

class AppDriver:

    global device
    #连接设备
    def device_connect(self):
        try:
            adb = ADB()
            devicesList = adb.devices()
            if (len(devicesList) >= 1):
                device = connect_device("android:///" + devicesList[0][0])
                #device = connect_device('Android://127.0.0.1:7555')
                return device
            else:
                device = None
                return device
        except AssertionError as e:
            print('error_info:',e)

    # 连接设备
    def device_connect_ios(self):
        try:
            tidevice = Usbmux()
            devicesList1 = tidevice.device_list()
            if (len(devicesList1) >= 1):
                #device = connect_device("iOS:///" + devicesList[0][0])
                device1 = connect_device("ios:///http://127.0.0.1:8100")
                # device = connect_device('Android://127.0.0.1:7555')
                return device1
            else:
                device1 = None
                return device1
        except AssertionError as e:
            print('error_info:', e)
    '''
    :return: 无
    '''
    #安装/卸载App
    def install_app(self,packageName):
        device=self.device_connect()
        if(device!=None):
            package_list = device.list_app(third_only=True)
            invalid_package_count=0
            for package in package_list:
                if package == packageName:
                    try:
                        #卸载旧包
                        uninstall(packageName)
                        sleep(2)
                        #安装新包
                        install(".\app\goodquestion.apk")
                        break
                    except AssertionError as e:
                        print('error_info:',e)
                else:
                    invalid_package_count+=1
                    if invalid_package_count == len(package_list):
                        try:
                            install(".\app\goodquestion.apk")
                        except AssertionError as e:
                            print('error_info:',e)
                    else:
                        print("未检测完成")
        else:
            print("未检测到连接设备")

    '''
    :param packageName[包名]:str
    :return: 无
    '''
    # Android端-启动APP
    def start_app_by_android(self,packageName):
        try:
            start_app(packageName)
            sleep(20)
        except AssertionError as e:
            print('error_info:',e)

    # iOS端-启动APP
    def start_app_by_ios(self,packageName):
        try:
            start_app(packageName)
            sleep(10)
        except AssertionError as e:
            print('error_info:',e)

    '''
    :param packageName[包名]:str
    :return: 无
    '''
    #Android端-关闭APP
    def stop_app_by_android(self,packageName):
        try:
            stop_app(packageName)
            sleep(5)
        except AssertionError as e:
            print('error_info:',e)

    #Ios端-关闭APP
    def stop_app_by_ios(self,packageName):
        try:
            stop_app(packageName)
            sleep(5)
        except AssertionError as e:
            print('error_info:',e)

    # Android端--清理APP
    def clear_app_by_android(self,packageName):
        try:
            clear_app(packageName)
            sleep(20)
        except AssertionError as e:
            print('error_info:',e)