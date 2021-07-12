"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: SearchPage.py
@time: 2021/1/23 19:00
@desc:

"""

from AppFrameWork.PageObject.Google.SnowBallMainPage import SnowBallMainPage


class SearchPage():

    def __init__(self, Locator, elements):
        self.Locator = Locator
        self.elements = elements

    def Search_display(self):
        """显示搜索内容"""
        self.element = self.elements["SearchPage"]
        self.Locator.click(self.element["content-desc"])
        return SnowBallMainPage(self.Locator, self.elements)


