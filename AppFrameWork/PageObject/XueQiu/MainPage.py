"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: MainPage.py
@time: 2021/1/24 20:28
@desc:
 * * * * * * 幸运女神保佑 * * * * * 永无BUG * * * * * * * * * * * * *
 *
 *                      .::::.
 *                    .::::::::.
 *                   :::::::::::
 *                ..:::::::::::'
 *             '::::::::::::'
 *               .::::::::::
 *          '::::::::::::::..
 *               ..::::::::::::.
 *             ``::::::::::::::::
 *              ::::``:::::::::'        .:::.
 *             ::::'   ':::::'       .::::::::.
 *           .::::'      ::::     .:::::::'::::.
 *          .:::'       :::::  .:::::::::' ':::::.
 *         .::'        :::::.:::::::::'      ':::::.
 *        .::'         ::::::::::::::'         ``::::.
 *    ...:::           ::::::::::::'              ``::.
 *   ```` ':.          ':::::::::'                  ::::..
 *                      '.:::::'                    ':'````..
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
"""
from AppFrameWork.PageObject.XueQiu.RegisterPage import RegisterPage
from AppFrameWork.PageObject.XueQiu.StockDetailPage import StockDetailPage


class MainPage:

    def __init__(self, Locator, elements):
        self.Locator = Locator
        self.elements = elements
        self.element = self.elements["MainPage"]


    def mainpage_search_function(self, value):
        self.Locator.click(self.element["search_text"])
        self.Locator.send_keys(self.element["input_text"], value)
        try:
            self.Locator.click(self.element["stock_search"])
        except:
            self.Locator.click(self.element["history_search"])
        self.Locator.click(self.element["stock_click"])
        return StockDetailPage(self.Locator, self.elements)


    def click_trade(self):
        self.Locator.click(self.element["click_trade"])
        return RegisterPage(self.Locator, self.elements)



