"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: MainPage
@time: 2020/12/29 23:52
@desc:
"""

from WebFrameWork.BasePage.BasePage import BasePage
from WebFrameWork.BasePage.Constant import Constants


class MainPage(BasePage):
    """百度首页"""

    datas = Constants().load_yaml('baidu')

    def search_function(self, value, url):
        """搜索功能"""
        data = self.datas["MainPage"]
        input_loc = data["input_loc"]
        click_loc = data["click_loc"]
        num_loc = data['search_sum']
        self.open_browser(url)
        self.send_keys(input_loc, value)
        self.click(click_loc)
        return self.locator_element(num_loc).text





if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    MainPage(driver, 'https://www.baidu.com/').search_function()


