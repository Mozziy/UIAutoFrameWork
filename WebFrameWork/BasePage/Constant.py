"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software: 
@file: Constant
@time: 2020/12/30 23:55
@desc: 固定参数值
"""
import os
from venv import logger

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Constants:
    """固定参数"""

    ROOT_PATH = os.path.realpath(__file__).split("BasePage")[0]
    DATA_DIR = os.path.join(ROOT_PATH, "Data")
    PAGE_ELE_DIR = os.path.join(DATA_DIR, 'PageElement')
    TEST_DATA_DIR = os.path.join(DATA_DIR, 'TestData')
    DRIVER_PATH = os.path.abspath(os.path.join(os.getcwd(), "../../../config/webdriver_path.yaml"))

    def load_yaml(self, project_name=None, module_name=None, path=PAGE_ELE_DIR):
        """加载配置文件"""
        DATA_PATH = os.path.join(path, f"{project_name}.yaml") if project_name else path
        try:
            with open(DATA_PATH, encoding='utf-8') as temp:
                datas = yaml.safe_load(temp)
            data = datas.get(module_name, None)

            return data if data else datas

        except:
            logger.error(F"此文件{DATA_PATH}不存在")


    def driver(self, broswer, runenv=None):
        """获取浏览器驱动"""
        browser_map = {
            "chrome": "Chrome",
            "fixfore": "Firefox",
            "safari": "Safari",
            "ie": "Ie"
            }
        broswer = browser_map.get(broswer.lower(), '')
        exe_path = self.load_yaml(module_name=broswer.lower(), path=self.DRIVER_PATH)
        if runenv:  # 无界面运行
            # 实例化一个启动参数对象
            chrome_options = Options()
            # 添加启动参数
            chrome_options.add_argument('--headless')
        else:
            chrome_options = None
        if hasattr(webdriver, broswer):
            return getattr(webdriver, broswer)(executable_path=exe_path, options=chrome_options)
        else:
            raise Exception(f"不支持该浏览器：{broswer}")



if __name__ == "__main__":
    y = Constants()
    print(y.DRIVER_PATH)


