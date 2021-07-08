"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: BasePage
@time: 2020/12/28 22:54
@desc:
              幸运女神保佑        永无BUG
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
"""


import time
import traceback
from venv import logger

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebFrameWork.BasePage.FakerGenerator import FakerGenerator
from WebFrameWork.BasePage.FindElement import FindElement, FindElements
from WebFrameWork.BasePage.DecorateComponent import black

class BasePage:

    def __init__(self, driver=None):
        self.driver = driver


    def chrome_remote(self, url):
        """谷歌浏览器复用"""
        # 若未打开浏览器，需要在terminal先执行命令[chrome]打开浏览器
        opt = webdriver.ChromeOptions()
        # 设置debug地址,默认：127.0.0.1:9222
        opt.debugger_address = url
        self.driver = webdriver.Chrome(options=opt)


    def open_browser(self, url):
        """打开浏览器"""
        self.driver.get(url)
        self.driver.maximize_window()



    def locator_element(self, loc: dict, single=True):
        """元素定位"""
        try:
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
            if hasattr(By, map_loc.get(list(loc.keys())[0], "")):
                locator = (getattr(By, map_loc[list(loc.keys())[0]]), list(loc.values())[0])
                # 保证元素可见
                logger.info(F"查找的元素和定位方法：{locator}")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
                return FindElement().__getattribute__(list(loc.keys())[0])(self.driver, loc[list(loc.keys())[0]]) if single \
                    else FindElements().__getattribute__(list(loc.keys())[0])(self.driver, loc[list(loc.keys())[0]])
            else:
                print("没有此定位方法%s" % (loc.keys()))
        except:
            traceback.print_exc()
            print("页面中没有%s元素" % (loc.values()))


    def send_keys(self, loc: dict, value, clear_first=True):
        """输入上传键盘操作"""
        try:
            logger.info(f"传入的值为：{value}")
            print(loc, value)
            self.click(loc)
            # 默认清空搜索框中的值
            if clear_first:
                self.locator_element(loc).clear()

        except:
            logger.warn("页面上未找到%s元素" % (loc.values()))

        finally:
            if value.startswith('random') and '_' in value:
                value = FakerGenerator(value)
            self.locator_element(loc).send_keys(value)


    def click(self, loc: dict):
        """点击操作"""
        self.locator_element(loc).click()


    def submit(self, loc):
        """提交表单，模拟回车键"""
        self.locator_element(loc).submit()


    def move_to_element(self, loc: dict):
        """鼠标悬停"""
        ActionChains(self.driver).move_to_element(self.locator_element(loc)).perform()


    def select(self, loc: dict):
        """下拉框"""
        return Select(self.locator_element(loc))


    def alert(self, loc: dict):
        """alert弹框"""
        # 获取alert对话框的按钮,点击按钮,弹出alert对话框
        self.click(loc)
        # 切换到alert对话框
        alert = self.driver.switch_to.alert()
        time.sleep(2)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        alert.accept()


    def confirm(self, loc: dict, choose=True):
        """confirm确认弹框"""
        self.click(loc)
        # 切换到alert对话框
        alert = self.driver.switch_to.alert()
        time.sleep(2)
        if choose:
            alert.accept()
        else:
            alert.dismiss()


    def prompt(self, loc: dict, value, choose=True):
        """prompt对话框"""
        self.click(loc)
        # 切换到alert对话框
        alert = self.driver.switch_to.alert()
        time.sleep(2)
        if choose:
            alert.send_keys(value)
            alert.accept()
        else:
            alert.dismiss()


    def java_script(self, src):
        """js定位执行"""
        self.driver.excute_script(src)
