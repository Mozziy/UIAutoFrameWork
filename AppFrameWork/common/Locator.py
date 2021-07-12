"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: Locator.py
@time: 2021/1/21 23:24
@desc:

"""
from venv import logger

from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from AppFrameWork.common.Constant import Constants
from WebFrameWork.BasePage.BasePage import FindElement, FindElements, BasePage


class Locator(BasePage):

    def __init__(self, project_name):
        super().__init__()
        conf_data = Constants().load_yaml(module_name=project_name)
        self.desire_map = conf_data.get("DesireMap", None)
        self.url = conf_data.get("url", None)
        self.driver = webdriver.Remote(self.url, self.desire_map)
        self.driver.implicitly_wait(60)

    def open_browser(self, url):
        """打开浏览器"""
        self.driver.get(url)

    def locator_element(self, loc: dict, single=True):
        map_loc = {
            "id": "ID",
            "name": "NAME",
            "cname": "CLASS_NAME",
            "tname": "TAG_NAME",
            "text": "LINK_TEXT",
            "ptext": "PARTIAL_LINK_TEXT",
            "css": "CSS_SELECTOR",
            "xpath": "XPATH"
        }
        if hasattr(MobileBy, map_loc.get(list(loc.keys())[0], "")) and list(loc.keys())[0] in list(map_loc.keys()):
            locator = (getattr(MobileBy, map_loc[list(loc.keys())[0]]), list(loc.values())[0])
            # 保证元素可见
            logger.info(F"查找的元素和定位方法：{locator}")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return FindElement().__getattribute__(list(loc.keys())[0])(self.driver, loc[list(loc.keys())[0]]) if single \
                else FindElements().__getattribute__(list(loc.keys())[0])(self.driver, loc[list(loc.keys())[0]])

        elif hasattr(MobileBy, list(loc.keys())[0]):
            locator = (getattr(MobileBy, list(loc.keys())[0]), list(loc.values())[0])
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator) if single else self.driver.find_elements(*locator)

        else:
            print("没有此定位方法%s" % (loc.keys()))


    def tuple_element(self, adict):
        if hasattr(MobileBy, list(adict.keys())[0]):
            return (getattr(MobileBy, list(adict.keys())[0]), list(adict.values())[0])
        else:
            raise Exception("没有此定位方法%s" % (adict.keys()))