"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: WorkPlace.py
@time: 2021/2/21 上午1:13
@desc:

"""
from time import sleep


class WorkPlace:

    def __init__(self, Locator, elements):
        self.Locator = Locator
        self.elements = elements


    def work_place(self):
        self.element = self.elements["Workplace"]
        self.Locator.locator_element(self.element["sign_in"]).click()
        self.Locator.click(self.element["Offsite_Punch"])
        sleep(2)
        self.Locator.click(self.element["click_Punch"])
        sleep(2)
        assert "外出打卡成功" in self.Locator.driver.page_source, "打卡失败"





