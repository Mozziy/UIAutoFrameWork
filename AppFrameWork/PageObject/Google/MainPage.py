"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: MainPage.py
@time: 2021/1/23 18:59
@desc:

"""
from AppFrameWork.PageObject.Google.SearchPage import SearchPage


class MainPage():

    def __init__(self, Locator, elements):
        self.Locator = Locator
        self.elements = elements


    def search_function(self, value):
        self.element = self.elements["MainPage"]
        self.Locator.click(self.element["click_input"])
        self.Locator.send_keys(self.element["input_value"], value)
        self.Locator.click(self.element["resource-id"])

        return SearchPage(self.Locator, self.elements)







