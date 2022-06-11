# -*- encoding=utf8 -*-
__author__ = "WLX"
#移动端-断言库
from airtest.core.api import *
import unittest

class AppAssert(unittest.TestCase):
    '''
    :param obj: UI元素对象
    :param msg: 测试点信息
    :return None
    '''
    #判断元素是否存在
    def assert_exists(self,obj,msg=None):
        try:
            unittest.TestCase.assertIsNotNone(self,obj,msg)
        except AssertionError:
            raise

    '''
    :param obj: UI元素对象
    :param msg: 测试点信息
    :return None
    '''
    #判断元素是否不存在
    def assert_not_exists(self,obj,msg=None):
        try:
            unittest.TestCase.assertIsNone(self, obj, msg)
        except AssertionError:
            raise

    '''
    :param imgPath: 图形路径
    :param msg: 测试点信息
    :return None
    '''
    #判断图形是否存在
    def assert_exists_by_img(self,imgPath,msg=None):
        try:
            is_img_exists = exists(Template(imgPath))
            unittest.TestCase.assertFalse(self, is_img_exists, msg)
        except AssertionError:
            raise

    '''
    :param imgPath: 图形路径
    :param msg: 测试点信息
    :return None
    '''
    #判断图形是否不存在
    def assert_not_exists_by_img(self,imgPath,msg=None):
        try:
            is_img_exists=exists(Template(imgPath))
            unittest.TestCase.assertFalse(self,is_img_exists,msg)
        except AssertionError:
            raise

    '''
    :param first: 实际值
    :param second: 预期值
    :param msg: 测试点信息
    :return None
    '''
    #判断两个值是否相等
    def assert_equal(self,first,second,msg=None):
        try:
            unittest.TestCase.assertEqual(self, first, second, msg)
        except AssertionError:
            raise

    '''
    :param first: 实际值
    :param second: 预期值
    :param msg: 测试点信息
    :return None
    '''
    #判断两个值不相等
    def assert_not_equal(self,first,second,msg=None):
        try:
            unittest.TestCase.assertNotEqual(self,first,second,msg)
        except AssertionError:
            raise

    '''
    :param a: 数值a
    :param b: 数值b
    :param msg: 测试点信息
    '''
    #判断a>b
    def assert_greater(self, a, b, msg=None):
        try:
            unittest.TestCase.assertGreater(self, a, b, msg)
        except AssertionError:
            raise

    '''
    :param a: 数值a
    :param b: 数值b
    :param msg: 测试点信息
    '''
    # 判断a>=b
    def assert_greater_equal(self, a, b, msg=None):
        try:
            unittest.TestCase.assertGreaterEqual(self, a, b, msg)
        except AssertionError:
            raise

    '''
    :param a: 数值a
    :param b: 数值b
    :param msg: 测试点信息
    '''
    # 判断a<b
    def assert_less(self, a, b, msg=None):
        try:
            unittest.TestCase.assertLess(self, a, b, msg)
        except AssertionError:
            raise

    '''
    :param a: 数值a
    :param b: 数值b
    :param msg: 测试点信息
    '''
    # 判断a<=b
    def assert_less_equal(self, a, b, msg=None):
        try:
            unittest.TestCase.assertLessEqual(self, a, b, msg)
        except AssertionError:
            raise