"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: FindElement
@time: 2020/12/30 00:21
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

from selenium.webdriver.common.by import By

class FindElement:


    @staticmethod
    def id(driver, ele):
        """id定位"""
        return driver.find_element(By.ID, ele)

    @staticmethod
    def name(driver, ele):
        """name定位"""
        return driver.find_element(By.ID, ele)

    @staticmethod
    def cname(driver, ele):
        """class_name定位"""
        return driver.find_element(By.CLASS_NAME, ele)

    @staticmethod
    def tname(driver, ele):
        """tag_name定位"""
        return driver.find_element(By.TAG_NAME, ele)

    @staticmethod
    def text(driver, ele):
        """LINK_TEXT定位"""
        return driver.find_element(By.LINK_TEXT, ele)

    @staticmethod
    def ptext(driver, ele):
        """PARTIAL_LINK_TEXT定位"""
        return driver.find_element(By.PARTIAL_LINK_TEXT, ele)

    @staticmethod
    def css(driver, ele):
        """css定位"""
        return driver.find_element(By.CSS_SELECTOR, ele)

    @staticmethod
    def xpath(driver, ele):
        """xpath定位"""
        return driver.find_element(By.XPATH, ele)


class FindElements:


    @staticmethod
    def id(driver, ele):
        """id定位"""
        return driver.find_elements(By.ID, ele)

    @staticmethod
    def name(driver, ele):
        """name定位"""
        return driver.find_elements(By.ID, ele)

    @staticmethod
    def cname(driver, ele):
        """class_name定位"""
        return driver.find_elements(By.CLASS_NAME, ele)

    @staticmethod
    def tname(driver, ele):
        """tag_name定位"""
        return driver.find_elements(By.TAG_NAME, ele)

    @staticmethod
    def text(driver, ele):
        """LINK_TEXT定位"""
        return driver.find_elements(By.LINK_TEXT, ele)

    @staticmethod
    def ptext(driver, ele):
        """PARTIAL_LINK_TEXT定位"""
        return driver.find_elements(By.PARTIAL_LINK_TEXT, ele)

    @staticmethod
    def css(driver, ele):
        """css定位"""
        return driver.find_elements(By.CSS_SELECTOR, ele)

    @staticmethod
    def xpath(driver, ele):
        """xpath定位"""
        return driver.find_elements(By.XPATH, ele)
