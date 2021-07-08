"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: MainPage.py
@time: 2021/2/20 上午12:11
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
from AppFrameWork.PageObject.WeWork.Contact import Contact
from AppFrameWork.PageObject.WeWork.WorkPlace import WorkPlace


class MainPage:

    def __init__(self, Locator, elements):
        self.Locator = Locator
        self.elements = elements
        self.element = self.elements["Message"]


    def main_page(self):
        self.Locator.click(self.element["workplace"])
        return WorkPlace(self.Locator, self.elements)

    def main_contact(self):
        self.Locator.click(self.element["contact"])
        return Contact(self.Locator, self.elements)
