"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: SnowBallMainPage.py
@time: 2021/1/23 19:01
@desc:

"""

class SnowBallMainPage():

    def __init__(self, Locator, elements):
        self.Locator = Locator
        self.elements = elements

    def download_snow_ball(self):
        """xxxx"""
        self.element = self.elements["SnowBallMainPage"]
        self.Locator.click(self.element["content-desc"])
        self.Locator.click(self.element["resource-id"])
        self.Locator.click(self.element["text_Download"])
        return 123

    def cancel_snow_ball(self):
        """xxxx"""
        self.element = self.elements["SnowBallMainPage"]
        self.Locator.click(self.element["content-desc"])
        self.Locator.click(self.element["resource-id"])
        self.Locator.click(self.element["text_Download"])

        return 123
