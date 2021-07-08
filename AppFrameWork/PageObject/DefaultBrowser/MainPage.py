"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: MainPage.py
@time: 2021/1/28 22:45
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
import time

from AppFrameWork.common.Constant import Constants


class MainPage:

    def __init__(self, Locator, elements):
        self.Locator = Locator
        self.elements = elements
        self.datas = Constants().load_yaml(project_name='DefaultBrowser', path=Constants.PAGE_ELE_DIR)

    def go_to_main(self, value):
        self.data = self.datas['Googlemainpage']
        self.Locator.open_browser(self.data['url'])
        # self.Locator.driver.find_element_by_id(self.data['input_id']).click()
        # self.Locator.driver.find_element_by_id(self.data['input_id']).send_keys(value)
        # self.Locator.driver.find_element_by_id(self.data['button_id']).click()
        self.Locator.click(self.data['input_id'])
        self.Locator.send_keys(self.data['input_id'], value)
        self.Locator.click(self.data['button_id'])

    def go_xueqiu_main(self, phone, code):
        self.data = self.datas['snowballmainpage']
        self.Locator.open_browser(self.data["url"])
        self.Locator.click(self.data["strong"])
        print(self.Locator.driver.contexts, self.Locator.driver.current_context)
        self.Locator.driver.switch_to.context('NATIVE_APP')
        # print(self.Locator.driver.current_context)
        self.Locator.send_keys(self.data["phone_id"], phone)
        self.Locator.send_keys(self.data["code_id"], code)