"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: RegisterPage.py
@time: 2021/2/10 下午9:06
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
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegisterPage:

    def __init__(self, Locator, elements):
        self.Locator = Locator
        self.element = elements["RegisterPage"]


    def register_account(self, phone, code):
        """注册"""
        self.Locator.click(self.element["open_account"])
        # print(self.Locator.driver.contexts)
        # self.Locator.driver.switch_to.context(self.Locator.driver.contexts[-1])
        self.Locator.send_keys(self.element["phone_number"], phone)
        self.Locator.click(self.element["send_code"])
        self.Locator.send_keys(self.element["phone_code"], code)
        self.Locator.click(self.element["click_open"])




