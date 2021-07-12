"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: WeWork.py
@time: 2021/2/19 下午11:55
@desc:

"""
from AppFrameWork.PageObject.WeWork.MainPage import MainPage
from AppFrameWork.common.Constant import Constants
from AppFrameWork.common.Locator import Locator


class WeWork:

    def __init__(self):
        self.locator = Locator("WeWork")
        self.elements = Constants().load_yaml("WeWork", path=Constants.PAGE_ELE_DIR)

    def daka(self):
        """企业微信打卡"""
        return MainPage(self.locator, self.elements)


    def add(self):
        return MainPage(self.locator, self.elements)




