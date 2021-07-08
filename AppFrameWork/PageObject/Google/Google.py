"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: Google.py
@time: 2021/1/23 21:14
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
from AppFrameWork.PageObject.Google.MainPage import MainPage
from AppFrameWork.common.Locator import Locator
from AppFrameWork.common.Constant import Constants

class Google:

    locator = Locator('Google')
    elements = Constants().load_yaml('Google', path=Constants.PAGE_ELE_DIR)

    def search_function(self):
        """谷歌搜索"""
        return MainPage(self.locator, self.elements)




