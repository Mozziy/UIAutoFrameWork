"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: test_grid.py
@time: 2021/3/6 下午1:16
@desc:

"""
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

class TestGrid:

    def test_grid(self):
        hub_url = "http://127.0.0.1:4444/wd/hub"
        # 官网建议使用copy，深拷贝--不会改变组件中的内容
        capability = DesiredCapabilities.CHROME.copy()
        for i in range(1, 5):
            driver = Remote(command_executor=hub_url, desired_capabilities=capability)
            driver.get('https://ceshiren.com/t/topic/5528')
