"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: StockDetailPage.py
@time: 2021/1/24 20:32
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


class StockDetailPage:

    def __init__(self, Locator, elements):
        self.Locator = Locator
        self.elements = elements


    def get_stock_price(self):
        self.element = self.elements["StockDetailPage"]
        try:
            self.Locator.click(self.element["choose_loc"])
        except:
            self.Locator.click(self.element["set_choose"])
            self.Locator.click(self.element["del_choose"])
            self.Locator.click(self.element["choose_loc"])
        return self.Locator.locator_element(self.element["stock_price"]).text




