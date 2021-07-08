"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: GetTestInfo.py
@time: 2021/1/2 16:03
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

from selenium import webdriver
from WebFrameWork.BasePage.BasePage import BasePage

class GetTestInfo:
    """获取测试信息"""

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base = BasePage(self.driver)

    def get_cookie(self, url):
        """获取cookie值"""
        self.base.open_browser(url)
        sleep(5)
        cookies = self.driver.get_cookies()
        sleep(2)
        print(cookies)


if __name__ == "__main__":
    GetTestInfo().get_cookie("https://work.weixin.qq.com/wework_admin/frame#index")

