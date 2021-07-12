"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: XueQiu.py
@time: 2021/1/24 19:43
@desc:

"""
from AppFrameWork.PageObject.XueQiu.MainPage import MainPage
from AppFrameWork.common.Constant import Constants
from AppFrameWork.common.Locator import Locator


class XueQiu:

    locator = Locator('XueQiu')
    elements = Constants().load_yaml('XueQiu', path=Constants.PAGE_ELE_DIR)

    def search_function(self):

        return MainPage(self.locator, self.elements)




